#相当于app.py 创建命令脚本来启动项目
from flask_script import Manager
from flask_migrate import MigrateCommand
from twittor import create_app

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()