# There is a better API framework for IcodeYoudao now, and TuringAPI is out of support.  
# [IcodeAPI is here](https://pypi.org/project/icodeapi/)  
------
## TuringAPI, the API framework for IcodeYoudao.  
You can use TuringAPI to control your account on IcodeYoudao.  
```python
from turingAPI-final import icodeUser
user = icodeUser(input('Enter cookie: ')) # login
print(user.info)  # user info
```
You can use `turingAPI.task`, `turingAPI.event` and `turingAPI.eventPool` to concurrent.  
```python
import turingAPI-final as turingAPI
user = turingAPI.icodeUser(input('Enter cookie: '))
ev = turingAPI.event(name='view')
for i in range(100):
    turingAPI.addTask(ev,user.getWorkDetail,'get{num}'.format(i),['66a116af4ade4abb97cc2bab3d57573f'],{})
ev.run()
```
Learn more in documents:  
[TuringAPI](https://xbz-studio.gitbook.io/turingapi)  
[Github](https://github.com/xbzstudio/TuringAPI)  