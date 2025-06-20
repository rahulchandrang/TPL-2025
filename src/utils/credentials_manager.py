from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

class CredentialsManager:
    def __init__(self, key_vault_name):
        self.key_vault_url = f"https://{key_vault_name}.vault.azure.net/"
        self.credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=self.key_vault_url, credential=self.credential)

    def get_secret(self, secret_name):
        try:
            secret = self.client.get_secret(secret_name)
            return secret.value
        except Exception as e:
            raise Exception(f"Error retrieving secret {secret_name}: {str(e)}")

    def load_env_variables(self, env_file_path):
        if os.path.exists(env_file_path):
            with open(env_file_path) as f:
                for line in f:
                    if line.strip() and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        os.environ[key] = value
        else:
            raise FileNotFoundError(f"{env_file_path} not found.")

    def load_secrets_to_env(self, secret_names):
        """
        Loads secrets from Azure Key Vault and sets them as environment variables.
        :param secret_names: List of secret names to fetch from Key Vault.
        """
        for secret_name in secret_names:
            secret_value = self.get_secret(secret_name)
            os.environ[secret_name] = secret_value

    def get_config(self, key, default=None):
        """
        Retrieves configuration from environment variables, falling back to default if not set.
        """
        return os.environ.get(key, default)