import Beeline    from "/static/js/kspda/classfile/beeline.js";
import Yomi       from "/static/js/kspda/classfile/yomi.js";
import TimerClass from "/static/js/kspda/classfile/timerClass.js";
import textDictsJson from "/static/json/DD.json" assert {type: "json"}

//gameで使う変数
var gamePlaying = false
var ACcount  = 0
var typemiss = false
var bgLevel = 1
var gameBgDom = document.getElementById("gameBG")
gameBgDom.style.background = `url("../static/img/kspda/bg${String(bgLevel)}.jpg")`

/* TimerClass */
var timerClass = new TimerClass(1, 0)
var timeDom    = document.getElementsByClassName("time")[0]
timeDom.textContent = timerClass.getTime()

var textDictsList = []
console.log(textDictsList)

//問題文のdomを取得
var textDictsListIndex = 0
var textdom          = document.getElementsByClassName("text")[0];
var textYOMIdom      = document.getElementsByClassName("textYOMI")[0];
var textPushSpaceDom = document.getElementsByClassName("pushSpace")[0];
var beelines = []


document.addEventListener("keypress", (e)=>{
    /*---------------------始まった時---------------------*/
    if(e.key == " " & gamePlaying==false){
        textDictsList = arrayShuffle(textDictsJson)
        gamePlaying = true
        textDictsList = arrayShuffle(textDictsJson)
        beelines = createBeelines(textDictsList[textDictsListIndex])
        timerClass.reset()
        textPushSpaceDom.innerHTML = ""
        bgLevel = 1
        gameBgDom.style.background = `url("../static/img/kspda/bg${String(bgLevel)}.jpg")`
    }
})

//何かしらのキーが押された時に動く
var targetTextIndex = 0
document.addEventListener("keypress", (e)=>{
    if (gamePlaying==false || e.key == " "){
        return
    }

    let targetYomiChar = beelines[targetTextIndex].getTargetYomiChar()
    console.log(targetYomiChar)
    if (e.key == targetYomiChar){
        //打った文字(YOMI)の色を変える
        let id = beelines[targetTextIndex].getTargetYomiID()
        document.getElementById('textYOMI'+id).classList.add("nyuuryoku")        

        //もしその文字の読みがすべて変わったらその色も返る
        if(beelines[targetTextIndex].checkLastYomi(id)){
            document.getElementById('text'+String(beelines[targetTextIndex].selfID)).classList.add("nyuuryoku")
            targetTextIndex += 1   
        }

        //もし最後の文字なら次の問題へ
        if (beelines.length == targetTextIndex){
            targetTextIndex = 0
            targetTextIndex = 0
            textdom.innerHTML = ""
            textYOMIdom.innerHTML = ""
            if (textDictsListIndex==26){
                finFlag = true
                return
            }
            textDictsListIndex += 1
            beelines = createBeelines(textDictsList[textDictsListIndex])

            //ACなら
            if(typemiss==false){
                ACcount += 1
                if (ACcount % 3 != 0){
                    if (ACcount == 10){
                        bonusRemove(9)
                        ACcount = 1
                    }
                    document.getElementById("bonus"+String(ACcount)).classList.add("ACbonus")
                }else{
                    if(ACcount % 9 == 0){
                    //ACSuperSpecialbonusなら
                    document.getElementById("bonus"+String(ACcount)).classList.add("ACSuperSpecialbonus")
                    timerClass.secondUp(3)
                    timeDom.textContent = timerClass.getTime()
                    //背景を次へ
                    bgLevel += 1
                    gameBgDom.style.background = `url("../static/img/kspda/bg${String(bgLevel)}.jpg")`

                    }else{
                    //superBonusなら
                    document.getElementById("bonus"+String(ACcount)).classList.add("ACSuperbonus")
                    timerClass.secondUp(1)
                    timeDom.textContent = timerClass.getTime()
                    }
                }

            }
            typemiss = false
        }
    }else{
        /*------------------missしたとき---------------------*/
        typemiss = true
        bonusRemove(ACcount)
        ACcount = 0
    }
});

//Timerの一秒ごとの処理
var timeFunc = setInterval(()=>{
    if (gamePlaying == false){
        return
    }

    timerClass.second1Down()
    let time = timerClass.getTime()
    timeDom.textContent = time
    console.log(time)
    if (time == "0:00"){
        /*---------------------終わった時---------------------*/
        gamePlaying = false
        textdom.innerHTML = ""
        textYOMIdom.innerHTML = ""
        textDictsListIndex = 0
        targetTextIndex = 0
        bonusRemove(ACcount)
        ACcount = 0
        typemiss = false
        bgLevel = 1
        document.getElementsByClassName("pushSpace")[0].innerHTML = "push Space"
    }
}, 1000)


//問題文のBeelinesを作りつつ、HTMLにapanタグを追加する
function createBeelines(textDicts){

    var textYOMIID = 0
    var textID = 0
    var beelines = []
    for(let textDict of textDicts){
        let yomis = []
        for(let char of textDict["YOMI"]){
            yomis.push(new Yomi(char,textYOMIID))
            textYOMIdom.innerHTML+=`<span id="${'textYOMI'+textYOMIID}">${char}</span>`
            textYOMIID += 1
        }

        beelines.push(new Beeline(textDict["char"], yomis, textID))
        textdom.innerHTML+=`<span id="${'text'+textID}">${textDict["char"]}</span>`
        textID += 1
    }
    return beelines
}

function bonusRemove(ACcount){
    for(let idNum of Array.from(Array(ACcount).keys())){
        if ((idNum+1) % 3 != 0){
            document.getElementById("bonus"+String(idNum+1)).classList.remove("ACbonus")
        }else{
            if((idNum+1) % 9 == 0){
            //ACSuperSpecialbonusなら
            document.getElementById("bonus"+String(idNum+1)).classList.remove("ACSuperSpecialbonus")
            }else{
            //superBonusなら
            document.getElementById("bonus"+String(idNum+1)).classList.remove("ACSuperbonus")
            }
        }
    }
}

//シャッフル
function arrayShuffle(array) {
    for(let i = (array.length - 1); 0 < i; i--){
  
      // 0〜(i+1)の範囲で値を取得
      let r = Math.floor(Math.random() * (i + 1));
  
      // 要素の並び替えを実行
      let tmp = array[i];
      array[i] = array[r];
      array[r] = tmp;
    }
    return array;
  }