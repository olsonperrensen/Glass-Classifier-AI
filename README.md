# Glass-Classifier-AI
### by [Max Iturria](https://github.com/olsonperrensen) ([r0834721](https://github.com/olsonperrensen))
<br>
<h6>Machine learning with Django</h6>
<br>
<p>This project uses Sai Prakash Reddy's Random Forest Classifier as inspiration. It is meant to distinguish different types of glasses depending on their chemical composition. </p>
<p>In order to run it, use the following command at the top-level directory of this project (/): </p>
<code>docker-compose up</code>
<hr>
<pre>Explanation:</pre>
<pre>There are two containers that deal with this app. 
The first one is an utility container and allows us to 
get the trained model based on .csv data in a .sav file. 
This container would normally be isolated and could 
not share that file with another contaier unless they 
were on the same network.</pre>
<pre>By using docker-compose, this gets done for us instead. 
As long as you have either a bind mount (during development) or 
a named volume where both containers can utilize it to get and 
write data to it, the linking between these two containers now becomes 
possible.</pre>
<pre>The second container is a web server written in Django with some
own tweaks in order to make it work. It is very precarious when it 
comes to architectural design and styling, but those were not the 
main goals my project intended to show. This Django container 
basically waits until the model has been completed... then looks 
for that .sav file and renders output based on its trained function. 
This is only possible thanks to both containers being linked through 
a bind mount on /Model.
Normally Django is not allowed to fetch files outside its directory, 
so I had to tweak the settings.py in order to do so. </pre>

# Give it a try! Go to [localhost:8000](http://localhost:8000) and see the results.
