from models.change import ChangeSchema, ChangeSeeder
from models.users import User
from models.song import song

ChangeSchema.run()
ChangeSeeder.run()

# User.all()
# User.get()