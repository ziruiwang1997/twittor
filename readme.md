### 登陆
```bash
sudo su - root
cd /home/ubuntu/twittor
```




### 启动工程
```bash
git pull
docker-compose up --remove-orphans -d 
```



 
### 如果无法启动服务
```bash
sudo systemctl daemon-reload
systemctl restart  docker
```
