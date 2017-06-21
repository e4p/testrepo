
* This is a list
* It contains `some code` but not much


```java
/* HelloWorld.java
 */

public class HelloWorld
{
  public static void main(String[] args) {
    System.out.println("Hello World!");
  }
}
```


```.ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

# Another example?

Python example below but first paragraphs

just so you know ```this is code``` ok?

Also, `.python is code`.




```python
fileobject = io.BytesIO("Hello \n World!")
hello = fileobject.readline()
```

```shell
ls -l
```

```shell-out-exact
-rw-r----- 1 evanp eng 1088 Jun 21 13:32 mdparse.py
-rw-r----- 1 evanp eng   75 Jun 21 13:30 README.md
drwxr-x--- 2 evanp eng 4096 Jun 21 13:32 testdoc1
```

```shell
gsutil ls -l gs://evanpdev/phix
```


```shell-out-exact
 164281905  2017-06-16T23:47:08Z  gs://evanpdev/phix/ERR1039256_1.fastq.gz
 193289585  2017-06-16T23:47:20Z  gs://evanpdev/phix/ERR1039256_2.fastq.gz
    383937  2017-06-17T06:59:38Z  gs://evanpdev/phix/ERR1039261.fastq.gz
  15171301  2017-06-17T07:00:09Z  gs://evanpdev/phix/ERR1039261_1.fastq.gz
  17889794  2017-06-17T07:00:40Z  gs://evanpdev/phix/ERR1039261_2.fastq.gz
      5535  2017-06-18T19:22:36Z  gs://evanpdev/phix/JX913857.1.fa
     21533  2017-06-16T23:48:00Z  gs://evanpdev/phix/JX913857.1.gb
       275  2017-06-16T23:48:11Z  gs://evanpdev/phix/METADATA.txt
                                 gs://evanpdev/phix/public/
TOTAL: 8 objects, 391043865 bytes (372.93 MiB)
```



<div style="display:none" class="python setup">
import io
import sys
if sys.version[0] != '2':
  raise RuntimeError('must use py2')
</div>

<div hidden>
python
evanpdev=evanpdev
</div>
