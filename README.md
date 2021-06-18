## 有关本次创建过程的大体描述，可以参考https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html

## 在IAM界面创建Policy，用于Lambda执行角色的权限

![alt text](https://github.com/zhixueli/CreateBackupForRedis/blob/master/images/IAMPolicy.png?raw=true)

## 在IAM界面创建用于Lambda执行的角色，将上一步中创建的policy attach给这个新建的角色

![alt text](https://github.com/zhixueli/CreateBackupForRedis/blob/master/images/CreateRole1.png?raw=true)
![alt text](https://github.com/zhixueli/CreateBackupForRedis/blob/master/images/CreateRole2.png?raw=true)

## 在Lambda界面创建一个新的函数，将Execution Role配置为上一步创建的角色。有关函数调用Redis备份接口，请参考https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html#ElastiCache.Client.create_snapshot，参数中snapshot的名字可以加上时间戳，避免重名创建失败，同时也可以根据时间戳定期删除过久备份

![alt text](https://github.com/zhixueli/CreateBackupForRedis/blob/master/images/CreateLambda1.png?raw=true)
![alt text](https://github.com/zhixueli/CreateBackupForRedis/blob/master/images/CreateLambda2.png?raw=true)

## 在CloudWatch界面创建一个新的Event Rule，调整时间间隔，并将Target配置为上一步创建的Lambda函数

![alt text](https://github.com/zhixueli/CreateBackupForRedis/blob/master/images/CreateCloudWatchEvent.png?raw=true)

## 可以在Lambda函数界面的Monitor标签栏观察函数执行情况以及日志

![alt text](https://github.com/zhixueli/CreateBackupForRedis/blob/master/images/LambdaMonitor.png?raw=true)