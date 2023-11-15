import json
import warnings
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError

from dataset_sh_server.auth import decode_key, verify_password, hash_password, encode_key, generate_password


class RepoServerUserProfile(BaseModel):
    user: str
    hashed: str


class RepoServerConfig(BaseModel):
    require_auth: bool = False
    hostname: str = 'http://127.0.0.1:5000'
    users: List[RepoServerUserProfile] = Field(default_factory=list)
    secret: str = Field(default_factory=generate_password)

    @staticmethod
    def load_from_file(fp):
        try:
            with open(fp, 'r') as fin:
                return RepoServerConfig(**json.load(fin))
        except (FileNotFoundError, json.JSONDecodeError, ValidationError):
            warnings.warn('cannot load server config, using default config now ')
            return RepoServerConfig()

    def write_to_file(self, fp):
        with open(fp, 'w') as out:
            json.dump(self.model_dump(mode='json'), out, indent=4)

    @staticmethod
    def generate_key(username, password):
        return encode_key(username, password)

    def update_password(self, username, password):
        for u in self.users:
            if u.user == username:
                u.hashed = hash_password(password)
                return
        self.users.append(RepoServerUserProfile(
            user=username,
            hashed=hash_password(password)
        ))

    def verify_key(self, key) -> Optional[str]:
        username, password = decode_key(key)
        if self.verify_userpass(username, password):
            return username
        return None

    def verify_userpass(self, username, password) -> bool:
        u = self.get_user(username)
        if u:
            return verify_password(password, u.hashed)
        else:
            return False

    def get_user(self, username):
        for u in self.users:
            if u.user == username:
                return u
        return None
