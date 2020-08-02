### 登陆
```bash
sudo su - root
cd /home/ubuntu/twittor
```




### 启动工程
```bash
git pull
docker-compose up --remove-orphans 

```



 
### 如果无法启动服务
```bash
sudo systemctl daemon-reload
systemctl restart  docker

netstat -lanp | grep 3306 | awk '{print $7}' | awk -F '/' '{print $1}' | xargs kill -9
netstat -lanp | grep 8000 | awk '{print $7}' | awk -F '/' '{print $1}' | xargs kill -9
netstat -lanp | grep 80 | awk '{print $7}' | awk -F '/' '{print $1}' | xargs kill -9
```
