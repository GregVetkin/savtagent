
from modules.system import ActiveUsersCollector

users = ActiveUsersCollector().collect()

print(users)