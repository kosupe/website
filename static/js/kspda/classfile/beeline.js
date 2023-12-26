class Beeline {
    constructor(selfChar, yomis, selfID){
        this.selfChar = selfChar
        this.selfID   = selfID 
        this.targetYomiIndex = 0
        this.yomis = yomis
        this.lastID = String(this.yomis[this.yomis.length - 1].selfID)
    }

    getTargetYomiChar(){
        return this.yomis[this.targetYomiIndex].selfChar
    }

    getTargetYomiID(){
        var id = String(this.yomis[this.targetYomiIndex].selfID)
        this.targetYomiIndex += 1
        return id
    }

    checkLastYomi(id){
        if (id == this.lastID){
            return true
        }
        return false
    }
}
export default Beeline