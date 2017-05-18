# csvformatter
just simple stuff

this is a simple csv formatter because i felt like experimenting with generators and functional style (maps) in python

## usage

```bash
$ cat out.csv
kag@egi.gov,Todd,Obrien,60,Torev Place,Ustawsif,CO,24750
nesu@egifamza.net,Theodore,Foster,20,Hiklot Highway,Fevikmaf,TX,09382
epodiz@fego.io,Clyde,Owens,27,Bumcas Court,Evapitgi,CT,51773
vo@mul.edu,Brent,Hamilton,30,Altap Extension,Kouduf,AK,72631
unorudda@to.com,Alma,Fitzgerald,37,Zihhuv Drive,Taagemo,ND,40220
gu@saj.io,Ellen,Burns,53,Pucwap Extension,Jezafam,SD,94292
tovowsip@urjodal.co.uk,Tom,Schneider,39,Susboz Square,Mespiru,WV,59197
ri@su.gov,Jeremiah,Rodriquez,25,Dekco Avenue,Ibahamu,VT,04007
furesuh@gug.edu,Tillie,Allison,30,Ugse Trail,Rinerfa,SD,15187
ednok@sufho.co.uk,Harvey,Pearson,40,Nemo Court,Julazjez,NE,35834
```

```bash
$ ./main.py out.csv out.txt
rows =  (22, 8, 10, 2, 16, 8, 2, 5)
$ cat out.txt
|      kag@egi.gov       |   Todd   |   Obrien   | 60 |   Torev Place    | Ustawsif | CO | 24750 |
|   nesu@egifamza.net    | Theodore |   Foster   | 20 |  Hiklot Highway  | Fevikmaf | TX | 09382 |
|     epodiz@fego.io     |  Clyde   |   Owens    | 27 |   Bumcas Court   | Evapitgi | CT | 51773 |
|       vo@mul.edu       |  Brent   |  Hamilton  | 30 | Altap Extension  |  Kouduf  | AK | 72631 |
|    unorudda@to.com     |   Alma   | Fitzgerald | 37 |   Zihhuv Drive   | Taagemo  | ND | 40220 |
|       gu@saj.io        |  Ellen   |   Burns    | 53 | Pucwap Extension | Jezafam  | SD | 94292 |
| tovowsip@urjodal.co.uk |   Tom    | Schneider  | 39 |  Susboz Square   | Mespiru  | WV | 59197 |
|       ri@su.gov        | Jeremiah | Rodriquez  | 25 |   Dekco Avenue   | Ibahamu  | VT | 04007 |
|    furesuh@gug.edu     |  Tillie  |  Allison   | 30 |    Ugse Trail    | Rinerfa  | SD | 15187 |
|   ednok@sufho.co.uk    |  Harvey  |  Pearson   | 40 |    Nemo Court    | Julazjez | NE | 35834 |
```

usage is: `./main.py <in file> [<out file>]`
in case no <out file> is provided output is redirected to stdout.

## Testing
on my machine [this file found under the release tab](https://github.com/mabbamOG/csvformatter/releases/download/1.0/test.ppmd.7z) (60MB and 1000000 rows with 8 columns long at most `(25, 11, 11, 2, 16, 9, 2, 5)`) takes around 21s 

running it with pypy3 takes about 12s

running `column  -t --output-separator ' | ' -s ','  <out.csv >out.txt` takes around 8s
