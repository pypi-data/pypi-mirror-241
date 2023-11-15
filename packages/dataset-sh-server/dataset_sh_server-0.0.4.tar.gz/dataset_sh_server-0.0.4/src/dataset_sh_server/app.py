import binascii
import json
import os
import warnings
from functools import wraps

import jwt
from flask import Flask, jsonify, send_file, g, request, make_response
from head_switcher import install_to_flask, load_from_package_resources

from dataset_sh.io import DatasetStorageManager
from dataset_sh.utils.files import filesize

from dataset_sh_server.utils import generate_download_code_bash, generate_download_code_py
from .core import RepoServerConfig
from dataset_sh.typing.codegen import CodeGenerator


def load_frontend_assets():
    try:
        return load_from_package_resources('dataset_sh_server.assets', 'app-ui.frontend')
    except FileNotFoundError as e:
        return {
            'index.html': 'dataset.sh web interface is disabled.'
        }


DISABLE_UI = os.environ.get('DISABLE_DATASET_APP_UI', '0').lower() in ['true', '1']


def load_config(app):
    config_file = os.environ.get('DATASET_SH_SERVER_CONFIG_FILE', './dataset-sh-server-config.json')

    if config_file is None or not os.path.exists(config_file):
        if not os.path.exists(config_file):
            warnings.warn('server config do not exist, server will be using a default configuration file, '
                          'which may affect some functionality, consider create and modify a configuration file.')
        host = app.config.get('SERVER_NAME', 'localhost')
        port = app.config.get('SERVER_PORT', '5000')
        return RepoServerConfig(hostname=f'http://{host}:{port}')
    else:
        with open(config_file) as fd:
            return RepoServerConfig(**json.load(fd))


def create_app(manager=None, frontend_assets=None, config: RepoServerConfig = None):
    if manager is None:
        manager = DatasetStorageManager()

    app = Flask(__name__, static_folder=None)

    if config is None:
        config = load_config(app)

    if frontend_assets is None:
        if not DISABLE_UI:
            frontend_assets = load_frontend_assets()
        else:
            frontend_assets = {
                'index.html': "dataset.sh web ui is disabled"
            }

    if config.require_auth:
        cookie_name = 'X-DATASET-SH-SERVER-AUTH-TOKEN'

        @app.route('/api/login', methods=['POST'])
        def login():
            username = request.json.get('username')
            password = request.json.get('password')
            if config.verify_userpass(username, password):
                token = jwt.encode({
                    'username': username
                }, config.secret, algorithm="HS256")
                response = make_response(jsonify({'message': 'Login successful'}))
                response.set_cookie(cookie_name, token)
                return response
            else:
                return '', 401

        @app.route('/api/logout', methods=['POST'])
        def logout():
            response = make_response(jsonify({'message': 'Logout successful'}))
            response.delete_cookie(cookie_name)
            return response

        @app.before_request
        def before_request_func():
            g.current_user = None
            token = request.cookies.get(cookie_name)
            if token:
                try:
                    payload = jwt.decode(token, config.secret, algorithms=['HS256'])
                    g.current_user = payload['username']
                except jwt.ExpiredSignatureError:  # pragma: no cover
                    pass
                except jwt.InvalidTokenError:  # pragma: no cover
                    pass
            else:
                access_key = request.headers.get(cookie_name, None)
                if access_key is not None:
                    try:
                        g.current_user = config.verify_key(access_key)
                    except (json.decoder.JSONDecodeError, binascii.Error):
                        pass

    def require_auth(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if config.require_auth and g.current_user is None:
                return '', 401
            return f(*args, **kwargs)

        return decorated_function

    @app.route('/api/dataset', methods=['GET'])
    @require_auth
    def list_datasets():
        items = manager.list_datasets()
        return jsonify(items.model_dump(mode='json')), 200

    @app.route('/api/store', methods=['GET'])
    @require_auth
    def list_stores():
        items = manager.list_dataset_stores()
        return jsonify(items.model_dump(mode='json')), 200

    @app.route('/api/dataset/<namespace>', methods=['GET'])
    @require_auth
    def list_datasets_in_store(namespace):
        items = manager.list_datasets_in_store(namespace)
        return jsonify(items.model_dump(mode='json')), 200

    @app.route('/api/dataset/<namespace>/<dataset_name>/readme', methods=['GET'])
    @require_auth
    def get_dataset_readme(namespace, dataset_name):
        return manager.get_dataset_readme(namespace, dataset_name), 200

    @app.route('/api/dataset/<namespace>/<dataset_name>/remote-source', methods=['GET'])
    @require_auth
    def get_dataset_remote_source(namespace, dataset_name):
        source = manager.get_dataset_source_info(namespace, dataset_name)
        return jsonify(source.model_dump(mode='json')), 200

    @app.route('/api/dataset/<namespace>/<dataset_name>/meta', methods=['GET'])
    @require_auth
    def get_dataset_meta(namespace, dataset_name):
        meta = manager.get_dataset_meta(namespace, dataset_name)
        fp = manager.get_dataset_file_path(namespace, dataset_name)
        meta['fileSize'] = filesize(fp)
        return jsonify(meta), 200

    @app.route('/api/dataset/<namespace>/<dataset_name>/collection/<collection_name>/sample', methods=['GET'])
    @require_auth
    def get_collection_sample(namespace, dataset_name, collection_name):
        sample = manager.get_sample(namespace, dataset_name, collection_name)
        return jsonify(sample), 200

    @app.route('/api/dataset/<namespace>/<dataset_name>/collection/<collection_name>/code', methods=['GET'])
    @require_auth
    def get_collection_code(namespace, dataset_name, collection_name):
        code = manager.get_usage_code(namespace, dataset_name, collection_name)
        return {'code': code}, 200

    @app.route('/api/dataset/<namespace>/<dataset_name>/download-code', methods=['GET'])
    @require_auth
    def get_download_code(namespace, dataset_name):
        fullname = f"{namespace}/{dataset_name}"
        lang = request.values.get('lang', 'python')
        code = ''
        if lang == 'bash':
            code = generate_download_code_bash(config.hostname, fullname)
        if lang == 'python':
            code = generate_download_code_py(config.hostname, fullname)
        return {'code': code}, 200

    @app.route('/api/dataset/<namespace>/<dataset_name>/file', methods=['GET'])
    @require_auth
    def get_dataset_file(namespace, dataset_name):
        f = manager.get_dataset_file_path(namespace, dataset_name)
        if os.path.exists(f):
            return send_file(
                f,
                as_attachment=True,
                download_name=f"{namespace}_{dataset_name}.dataset"
            )
        return '', 404

    install_to_flask(frontend_assets, app)

    return app


if __name__ == '__main__':  # pragma: no cover
    _frontend_assets = {
        'index.html': "dataset.sh web ui is disabled"
    }

    if not DISABLE_UI:
        _frontend_assets = load_frontend_assets()

    app = create_app(frontend_assets=_frontend_assets)
