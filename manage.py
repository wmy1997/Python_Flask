from app import app
from flask_migrate import MigrateCommand,Migrate
from flask_script import Manager
from exts import db
from models import User
from models import Question

manage=Manager(app)

#使用migrate绑定app和db
migrate=Migrate(app,db)

#将MigrateCommand命令添加到manager中（迁移文件）
manage.add_command('db',MigrateCommand)

if __name__=='__main__':
    manage.run()