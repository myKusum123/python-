'''
Git- Git is a version control system
#Use
-To track every changes of our projects
-collaboration
-Branches
-Remote

First git bash download garni ani tes paxi
# Git bash ma run garni
1.$ cd c:
2.$ cd /Users/Dell/Documents/python/
3.$ cd test/
ma test folder ma aayem python ko ani
4.$ git init
$ git init- gardah chai green colour dekhxau tyo vaneko chai on track ho
$ git init-jun project git ma halnu parni ho tesko  jun folder hamilae track garnu xa 
ra change garnu xa tyo folder ma gayera git init garni yo le chae git initalized vayera 
git ko repositary  banxa  and.... ahmile file ma gayera folder ma gayera view ma gayera show  
ma hidden ma click  garyo vani hamile .git dekhna sakxau ani tyo folder le chai project
ya folder ma vako lai track ya change garxa so tyo floder(.git) nai yo project ko hamro repository ho

Repository- ko chai branch hunxa tyo vaneko chai project ko (copy) ho and master branch chai main branch ho jun
chai repository create gardah baneko hunxa 
Repository banepaxi master branch create hunxa
 jun pni folders ra file xa ni tyo repository vitra xaina kina ki yesma pni lifecycle xa buju  aba

 jun pni naya file ra folder banako hunxam tyo repository ma hunna jaba samma track gardae nau and repo.. vaneko xutai thau ho jba 
 hami git init garxau ni taba repo.. banxa ani hamile .git delete garyo vani repo.. delete hunxa

 # life cycle of Git
 1. Untracked-Add the file (yo vaneko chai repo.. lai yo file exit garxa vanera tha hunna project ma hunxa but repo.. ma huna)
 2.Stagged-commit
 3.Unmodified-Edit the file
 3.Modified
 jun chai folder haru track hunna teslai untracked vanxau ani add garera stage ma lagni and comit gare paxi tyo unmodified file banxa 
 jun chai track file ho and unmodified file lai change garem vani modified file banxa
 
 5.$ git add .- A vanera aauxa jun chai stage area ma pugyo and untracked file ya unmodified file lai chai track filr ma lagyo mtlb stage ma
lagyo and stage vaneko chai track garni area ho ($ git add le chai add garni track ma lagxa mtlb stage ma)
6. $ git commit-m 'new repo'-(-m= yo chai message ho) commit vaneko chai commit garni code ho and commit le chai add gareko ma k k change vako xa vanera define garni ho

7. again $ git add .
8.$ git commit-m 'new comment added'

#Git - programming ko software ho
 Git is a version control system or it manage the project system By using git we can track the project
Hmile kunai pni euta naya project banayo vani tyo project chai thulo huna sakxaani tes paxi
tyo project lai chai hamile gitma halyo vani tyo project ko different version lai hamile control garna milxa
vannale maile euta project banaye re any tyo projet ma chai j j xa ahile samma garnu parni tyo garera git
ma rakhni ani feri tyo project ma chai naya update rakhnu paryo vani chai tyo project ma chai nay update rakhera
naya version create garna milxa git ma ani maile tyo garpaxi chai purano version ma pni jana milxa
naya version ma pni jana milxa

Use
-To track every changes of our project
-Collaboration-euta project ma dherae jana le kam garna sakxa
-Branches- (copy)[project ko multiple copy ho and tyo copy ma chai different people le contribute garna milyo and contribution 
lai chai aafno project ya aafno copy wala branch lai chai merge ya update garna milxa]
-Remote- 
Repositery banayesi tesma branchh hunxa tyo vaneko chai repo.. ko multiple copy banau na milxa 
tei vayera change garna track garna milxa branch

jun file repo.. ma hudae na teslai untracked vanxa


untracked- (yo vaneko chai repo lai tha hudae na ki tyo file exit garxa ki nai vanera) 
add the file (yesle file lai add gardah chai track huna janxa and track (stage)hudah 
feri commit garyo vani chai tyo bela k k check vayo vanera define garni)
Stage-track change define
unmodified- yo vaneko chai repo lai thaxa file ra folder xa vanera tesma k he change gareko xaina



git add .- ( track garni area ma lagxa)staged area ma pugyo and git add . vaneko euta command ho jun lr chai untrack file lai stage ma lagxa
Stage - its means track garni area
git commit-m'new Repo'- yesle chai add gardah tesma k k change vako xa vani herxa ra define garxa
git add . - vaneko chai change garni ho
git commit-m'new Repo' -vaneko chai change gareko lai define garni ho
 '''
'''hamile $ git add 'how to use git.t' (quatation vitra rakheko chai kina ki space xa 
and yo file ma matra track gara vanera define garna  milxa repo ma..)
$ git add git.txt' yo chai quotation vitra rakhnu pardae na kina ki space xaina'
yeti gare si chai stage ma add garxa specific ffile lai tes paxi chai commit garni
$ git commit -m 'new files added' -and commit (define)garni ki kun files add garyo 
vanera ani jun file lai define gareko xa teslai white ma dekhau xa
git add - yo garyo vani chai specific file lai add garyo
git add . - yo garyo vani chai sab filr lai add garxa
commit- ma chai k k change gareko xa sab define ramro sanga garnu parxa like naya 
file haru ko name ''(double cotation ko citra rakhnu parxa) and commit gare paxi sab
unmodified hunxa hunxa and tyo file vitra lekhepaxi modified hunxa
U - vaneko chai Untracked file ho
M- modified
jun file lai add garnu xa  teslai $ git add 'git.txt' garni
natra sab file add garnu xa vani $ git add . ' copied git defination  and 
added in every file' rakhni
$ git log- hamile jati pni  change gareko xau add gareko ra commit gareko xau xau teslai 
herna ko lagi git log use garxau ani jati pni ahile gareko xau ni change girst ma dekhxau
and end aayo vani q click garera quet garxau

Repositery ma multiple branch create garna milxa and hamile jaba git init gareko hunxa
tesma already branch banxa master branch and master branch vaneko chai main branch ho automatically 
create hunxa and hamile jun branch ma chai basera kam garxau tyo branch ma hamile j j change 
garxau tyo branch ma matra basxa and hamile log ko kura garxau ni tyo pni divided hunxa 
branch anusar and sabai le master branch ma basera code gara vandae na
ani hamile multiple branch banau xau 
and module anusar ko hamile kam garni hunaale hamile xutta xuttai branch haru create garxa and
 hamile master branch ma chai kina code gardae nau vani kina ki hamile xutta xuttai module ko branch
banauxauand sab module ya branch lai jati pni changes ya add garxau telai combine ya merge garera euta 
whole project banau nu parxa tesaile master branch use gardae nau
new brach ko lagi
 $ git branch fd(fd chai new branch ko name)
 aba new branch ma gayera kam garna ko lagi chai
 $ git checkout fd(fd branch ma jana ko lagi)- hamile jun branch ma kam garyo tei ma matra files ra changes basxa ra hunxa aru branch ma changes ma hunna
# new branch made- master ma basera garni
and fd branch ma gareko change chai ph branch ma aakoxaina
 $ git checkout master(master branch ma jana ko lagi)
$ git branch ph
$ git log- yaha samma chai ph ko heryo logbut master ma baseko chai
 $ git checkout master
 git log garni

 $ git revert - tyo commit ko id  copy garni ani git revert ma paste garni ani tyo garepaxi
 tyo commit garnu vandah aagadi ko statement ma pugxa
 
 # merged
# if we want fd code in master branch then
$git checkout master
$ git merge fd (yestoh gardah  chai hamilai yedi kunai file ma k he lekheko xa vani tesma hamilai incoming ki current ki accept all vanera sodhxa)
then use $ git add.
$ git commit -m 'merged fd'

# if we want to put master code in fd code then (jun branch ma merge garna lako ho tyo branch ma basera merge  garni
$ git checkout fd
$ git merge master
$ git commit -m 'merged master'


# Git removed
$ git rm --cached git.txt(git.txt-file name) (yestoh garyo vani untracked file banxa)
$ git rm git.txt( yestoh garyo vani chai direct delete hunxa folder bata)

# Ignore
$touch .gitignore ((.)- vaneko chai hidden file ho)(bash vanni terminal ma chai naya file create garnu xa vani touch vanni command use garera . file ko name lekhnu parxa and hamile gitignore vanni file banayem)
and hamilai git ignore garnu xa vani terminal le banako file chaheni hunxa so hamile gitignore file banayem
$ git add .gitignore (gitignore chai add vayo repo ma)
gitignore(yesko kam chai file and folder lai chai ignore garnu ho and repo.. ma vako jati pni file hunxa tyo track nai hudae na)
$ git commit -m 'added gitignore file'
and aba hamile .gitignore file ma gayera kunai repo.. ko file(git.txt) name rakhyo vani gray aauxa 
$ git add .
$ commit -m 'ignore git.txt'  (yo gare paxi chai git.txt file chai ignore hunxa yesma ma vako kunai pni change garyo vani k he pni change hunna kina ki yo file ignore hunxa)
git ignore le chai untracked file haru lai matra ignore garni ho
and untracked garna chai $ git rm --cached git.txt yo command use garnu parxa
hamile gitignore kina use garxau vani paxi gyera django ma sab file lai track garnu parx vanni xaina jun chai hamilai chahenxa xa tyo file rakhni ani aru hamile ignore gardah hunxa gitignore garera
gitignore ma hamilai kunai pni folder ignore garnu xa vani hamile gitignore ma gayera /folder ko name lekhni example-/.py ani tya vaki file ra folder sab ignore hunxa
 aba hamilai .py ko folder vitra aru file ko euta matra ignore garnu xa vani tesko name gitignore ma gayera lekhni but tyo name aru pni folder ma xa vani tyo pni ignore hunxa so hamile tyo euta matra file lai ignore garnu lai hamile /foldername/file name lekhnu parini hunx example /.py/kusum


 git system ma hamile kina use garxau vani aba hamile dherae kura haru change garnu parni hunxa naya kura haru add garnu parni hunxa tyo sab kura haru lai chai track garnu parni hunxa kati khera k change hunxa sab or track garna lai like a super viser 
 another is collaboration

 first chai hamile git ko repo... banau nu paryo tesko lagi ahmile git init garxau
 ani and according to git tyo file ra folder chai   empty hunxa file haru chai repo.. vitra hunna kina ki hamile vakhar create gareko hunxau and untrack hunxa so untrack file lai chai git add. ra git commit garera track garna repo.. ma rakhdinxa tyo garesi chai tyo file and folder chai untrack
 bata track vayera unmodified hunxa and unmodified vayo vani chai  k he status  hudae na mtlb white hunxa file ko words and tyo file and folder ma k he lekheu ya change gareu vani modified hunxa and hmaile tes paxi add ra commit gari halnu parxa vanni xaina hamile bistarae sab lekhi sakepaxi change 
 garepaxi  add ra commit gardah hunxa  tyo garepaxi change chai track hunxa
  hamile every single file and folder ma chai change gardae gare paxi repo.. ma chai git log create hudae janxa and log herna ko lagi hamile git log garxau tyo garpaxi hamro jati pni commit xa hamile herna sakxau and end vaypaxi q click garni
  git reverd command le chai hamile commit ko id liyera copy garyo vani kun state ma thiyo commit gardah vaneraa tyos tate ma chai lagdixa
$git revert and copy of commit
commit gare paxi chai
git add.
git commit -m 'changes'
$ git branch -garyo vani yo repo ma kati ota branch xa vanera herna milxa
branch vaneko chai repo ko copy haru ho jun ma chai hamiledifferent branch ma different kam garna milxa 
$ git branch new - garyo vani new vanni branch create hunxa
hami jun branch ma hunxa tya green dekhau xa
jaha nira ! sign aauxa tyo chai error ho
 git ignore.....
 git hub sanga  link garni aba local repositery lai ahile samma hamile chai hamile repository create tw gareu but locally create gareu
 locally create gardah chai repo le chai files and folders lai matra track garna milxa tara files and folder ya whole project lai system bata hatayera
 remote ma rakhnu xa vani tyo hamile remote repository create garnu parxa
 remote repository create garna lai chai git hub create garnu parxa
 Git hub ma jani profile ma gayera setting ma jani tes paxi ssh and gpg keys ma jani tyo vaneko chai local repository lai chai remote ma link garni tyo garna chai ssh and gpgkey ma janu 
 parxa tyo pahilanai xa vani delete garera naya banau na milxa new ssh xa vani generate ssh keys blue line ma jani tay chai kk garni lekheko xa
 tespaxi generating a new ssh keys and adding it to the ssh -agent ma jani ani tyo first ko code xa(About SSH key passphrases-ssh-keygen -t ed25519 -C "your_email@example.com"
) ssh-key... something xa teslai copy garni ani
 git bash ma gayear $cd c: garera enter garera tyo code lai paste gardinu ani tya chai afno email rakhdini and enter garni
 tespaxi enter garni ani y/n aauxa y garni ani passphrase auuxa empty rakhdidah pni hunxa
 yo garesi chai ssh key generate vayo
 Adding your SSH key to the ssh-agent-(eval "$(ssh-agent -s)"-first yo code paste garniani run garni ani yo(ssh-add ~/.ssh/id_ed25519)- yo chai paste garni git bash ma
jun hamile email deko thiyeu tyo identity added vayo ani tes paxi 
"Adding a new SSH key to your GitHub account." ma jani git hub ko ani Copy the SSH public key to your clipboard.
ko code lai copy ($ clip < ~/.ssh/id_ed25519.pub)garni ani git bash ma paste garni ssh key lai chi copy gareko hamro account ma halna ko lagi
so hamro system ko chai ssh key generate vayo so yo system ma jati pni local repository create garxau teslai remote ma halna ko lagi chai tyo ssh key lai chai hamro account ma halnu oarxa]
tesko lagi chai git hub account ma gaye  new ssh key ma click gare tes pasi title ma Kusum Dell
ani key ma ctrl v garni $( clip < ~/.ssh/id_ed25519.pub) ani add keys garni ani password magxa
ani dashboard ma gayera profile ma gayera new ma click garni folder ko name lekhni public
garesi remote repository create hunca aba local tw hamro c disk  vitra Users/Dell/Documents/python/
tes paxi $ cd test/ $ cd project/ then after master ma jani $ git checkout master(sabai update code master ma halxau) first hamile git bash ma create garni ani git hub 
…or push an existing repository from the command line- yesko(git remote add origin https://github.com/myKusum123/python.git)copy garera git bash ma paste garni ani enter garni and tei ko (git push -u origin master)- paste garni git bash ma and main ko thau ma master rakhni

what is the relation between local and remote repository
sab same hunxa git add. , git ignore sab same hunxa but two kura chai xuttai hunxa lets talk
remote ra remote ko kam project ko changes haru lai track garnu ho
features of remote
-sabai changes haru git hub ma ramro sanga dekhna pauxau branch pni
-collobration pni garna milxa
-remote repo le aru ko repo.. haru pni herna milxa public ma rakheko haru ko
-two types of code push and pull
local- chai hamro system ma vako ho jun chai hamile aafai react garxau git add ra git comit garera 
remote-yo chai web ma hunxa mero account ma and hamile kasari garni tw react remote ma chai push ra pull garni 
local ma jati pni change gareko hunxa tyo chai remote ma lani tei paxi gayera local ma delete vaye pni remote ma hunna
remote ma chai jati pni add rachange gareko xa push garni
if remote ma chai change vayo re but local ma chai vako xaina vani teti khera hami pull garxau
push- yedi hamilai local ko change remote ma rakhnu xa vani push
pull yedi hamilai remote ko changes local ma rakhnu xa vani pull

then kunai file ma text haru add garni ani terminal ma powershell garni
git add.
git commit -m 'add texts in .py file- (.py-yo chai file)
git log
yeti chai local ma garni kam ho  ani yeti chai locally track vae sakyo but remote ma xaina
aba hamile yo remote ma pni tw change garnu paryo vani chai hamile git push garni
aba feri hamile remote ma gayera hereu change vako aba change vae saje paxi hamile k he change gareu re remote ma ab ak garni tw
hamile local ma gayera git pull garxau
yo chai hamile master branch ma gareko
aba aru branch ma gayera git checkout fd vanera aru branch pull ra push garna mildae na
 aba jati pni branch xa local ma tyo remote ma rakhna   chai -git push -u origin (and jun branch ko name remote ma rakhnu xa tyo branch ko name lekhni example)fd
aba fd branch chai git hub ma aayo
jun branch ma basera hamile kam gareko xa teha git push ra git pull garni

aba hamile yo folder delete gareu re aba remote matw basxa but hamile kosalai access dinu paryo k garni tw aafno profile ko setting ma gayera collaboration ma jani
password magxa halesi add people dekhauxa tesma gayera hamile koi hamro sathi haru lai access dina milxa
aba usle access payo aba locally tannu paryo aba uh chai code ma gayera ssh maclick garera copy garxaa and terminal kholera usko kun file ma rakhni tya gayera
cd c:
cd user/.....
#git clone  (and ssh ) vanni command  use garni and testoh garesi remote ma jastoh xa locally tesari basxa




Djaango vaneko chai backend ya api related ka ko lagi garxa
Django chai fullstack ho fronted pni garna milxa backend pni garna milxa but hami chai backend develop garxau

# Backend development
The process of developing backend of a website jati pni data related kam chai website ma euta user ko plan name haru store garxa develop garxa teslai nai backend vanxa
backend le chai website ko part lai store garxa control garxa create garxa delete garxa teslai nai backend development vanxa
# Fronted Development- hamile dekhna sakau and interreact garna milxa touch kholna etc
# Process
-planning- (requirement collection)aba euta k he kura develop garnu xa kunai app ko k he kura banau nu xa vani hami le planning garxau k k chahenxa tesma vanera
-Designing-Er diagram, flow diagram
1.Er diagram-jati pni data base table haru banxa ni backend banaudah tyo sab ko design ho 
2.flow diagra-- kasari data haru create garni
-programming-python(programming language)and django(framework-tool ho jaslai use garera certain kura build garxau)
-Debugging
-Deployment
# Django- python,web framework
#Templates(fullstack)-fronted -todo project
#API(Backend)-(Inventry Management system)-both frontend ra backend communicate garna ko lagi api use hunxa

#Battery included framework
#Fullstack-MVT(Model View Template)
#Model-Database implementation (database-it is a actual place where we can store the data)-database ma k k hunxa ani feld kastoh kastoh hunxa
#View-Data controller(create, delete, calculate)
#Templete-Fronted, fronted  data implementation

#API-backend ra fronted lai communicate garna help garxa
#serializer-converts object into json format(yedi hamile backend bata fronted ma data pathai raxau vani json format ma pathau nu parxa)(yedi hamile fronted bata backend ma data pathai raxau vani json format ma pathau nu parxa json format ma lana chai serializer vanni compomnent aafai create garera use garxau )
 
to download django
cmd- pip inatsall Django  
#env- environment ho josle module haru store garxa project ma
c:
cd Users\Dell\Documents\python
cd test
django-admin starproject ToDo (- startproject vanni command use garera django ko project start garxau and ToDo chai name define gareko ho ToDo ma space hunu vayena
cd ToDo
python manage.py runserver- yo vaneko chai hamro project lai server ma run gareko
tes paxi yo aauxa  http://127.0.0.1:8000/- yo chai hamile yo project  chalaunjel samma matra run garna milxa
and hamile ctrl break garyo vani yo 127.0.0.1:8000 local server  mA run gareko pni janxa
tespaxi
install virtualenv-yesle chai env module create garxa
virtualenv kusum (or env)- 
env\scripts\activate
pip install django- project ma djanjo chahene vayera  install vayo

'''

# new 