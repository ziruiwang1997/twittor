### 登陆
```bash
sudo su - root
cd /home/ubuntu/twittor
```




### 更新工程
```bash
git pull
```


### 启动工程
```bash
docker-compose up --remove-orphans -d 
```



 
### 如果无法启动服务
```bash
sudo systemctl daemon-reload
systemctl restart  docker
```
