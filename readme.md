###登陆
sudo su - root
cd /home/ubuntu/twittor#



### 更新工程
git pull

### 启动工程
docker-compose up --remove-orphans -d 


 
### 如果无法启动服务
sudo systemctl daemon-reload
systemctl restart  docker