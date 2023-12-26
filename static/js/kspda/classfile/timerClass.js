class TimerClass{
    constructor(minutesNum,secondNum){
        this._minutesNum = minutesNum
        this._secondNum = secondNum
        this._startMinutesNum = minutesNum
        this._startsecondNum  = secondNum
    }

    //カウントアップ
    secondUp(upSecond){
        this._secondNum += upSecond
        if (this._secondNum >= 60){
            this.minutesUp()
            this._secondNum -= 60 
        }
    }

    minutesUp(){
        this._minutesNum += 1
    }


    //カウントダウン
    second1Down(){
        if (this._secondNum == 0){
            if (this._minutesNum > 0){
                this.minutesDown()
                this._secondNum = 59
            }
            return
        }

        this._secondNum -= 1
    }

    minutesDown(){
        this._minutesNum -= 1
    }


    getTime(){
        let minutes = ""
        let second  = ""

        minutes = String(this._minutesNum)

        if (this._secondNum < 10){
            second = "0"+String(this._secondNum)
        }else{
            second = String(this._secondNum)
        }

        return minutes+":"+second
    }

    reset(){
        this._minutesNum = this._startMinutesNum
        this._secondNum  = this._startsecondNum + 1
    }
}

export default TimerClass