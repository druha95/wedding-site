/**********************************************************************************************
* Day Counter script by Praveen Lobo (http://PraveenLobo.com/techblog/javascript-counter-count-days/)
* This notice MUST stay intact(in both JS file and SCRIPT tag) for legal use.
* http://praveenlobo.com/blog/disclaimer/
**********************************************************************************************/

function DayCounter1(initDate, id){
    this.beginDate = new Date(initDate);
    this.container = document.getElementById(id);
    this.calculate();
}
  
DayCounter1.prototype.calculate=function(){
    var secDiff = Math.round(((new Date()) - this.beginDate)/1000);
    var nextUpdate = 86400 - (secDiff % 86400);
    var tmp = (tmp = secDiff/86400) < 1? 0 : Math.floor(tmp);
    var days = (tmp < 10 ? ("00" + tmp) : tmp < 100 ? ("0" + tmp) : tmp);
    this.container.innerHTML = 
        "<strong>" + days + "</strong> " + (days == 1? "day" : "Tagen");
    var self = this;
    setTimeout(function(){self.calculate();}, (++nextUpdate*1000));
}


function DayCounter2(initDate, id){
    this.beginDate = new Date(initDate);
    this.container = document.getElementById(id);
    this.calculate();
}
  
DayCounter2.prototype.calculate=function(){
    var secDiff = Math.round(((new Date()) - this.beginDate)/1000);
    var nextUpdate = 86400 - (secDiff % 86400);
    var tmp = (tmp = secDiff/86400) < 1? 0 : Math.floor(tmp);
    var days = (tmp < 10 ? ("00" + tmp) : tmp < 100 ? ("0" + tmp) : tmp);
    this.container.innerHTML = 
        "<strong>" + days + "</strong> " + (days == 1? "day" : "Tagen");
    var self = this;
    setTimeout(function(){self.calculate();}, (++nextUpdate*1000));
}


function HourCounter1(initDate, id){
    this.beginDate = new Date(initDate);
    this.container = document.getElementById(id);
    this.calculate();
}
  
HourCounter1.prototype.calculate=function(){
    var secDiff = Math.round(((new Date()) - this.beginDate)/1000);
    var nextUpdate = 86400 - (secDiff % 86400);
    var tmp = (tmp = secDiff/3600) < 1? 0 : Math.floor(tmp);
    var days = (tmp < 10 ? ("00" + tmp) : tmp < 100 ? ("0" + tmp) : tmp);
    this.container.innerHTML = 
        "= <strong>" + days + "</strong> " + (days == 1? "day" : "Stunden");
    var self = this;
    setTimeout(function(){self.calculate();}, (++nextUpdate*1000));
}

function HourCounter2(initDate, id){
    this.beginDate = new Date(initDate);
    this.container = document.getElementById(id);
    this.calculate();
}

  
HourCounter2.prototype.calculate=function(){
    var secDiff = Math.round(((new Date()) - this.beginDate)/1000);
    var nextUpdate = 86400 - (secDiff % 86400);
    var tmp = (tmp = secDiff/3600) < 1? 0 : Math.floor(tmp);
    var days = (tmp < 10 ? ("00" + tmp) : tmp < 100 ? ("0" + tmp) : tmp);
    this.container.innerHTML = 
        "= <strong>" + days + "</strong> " + (days == 1? "day" : "Stunden");
    var self = this;
    setTimeout(function(){self.calculate();}, (++nextUpdate*1000));
}


function MinuteCounter1(initDate, id){
    this.beginDate = new Date(initDate);
    this.container = document.getElementById(id);
    this.calculate();
}
  
MinuteCounter1.prototype.calculate=function(){
    var secDiff = Math.round(((new Date()) - this.beginDate)/1000);
    var nextUpdate = 86400 - (secDiff % 86400);
    var tmp = (tmp = secDiff/60) < 1? 0 : Math.floor(tmp);
    var days = (tmp < 10 ? ("00" + tmp) : tmp < 100 ? ("0" + tmp) : tmp);
    this.container.innerHTML = 
        "= <strong>" + days + "</strong> " + (days == 1? "day" : "Minuten");
    var self = this;
    setTimeout(function(){self.calculate();}, (++nextUpdate*1000));
}

function MinuteCounter2(initDate, id){
    this.beginDate = new Date(initDate);
    this.container = document.getElementById(id);
    this.calculate();
}
  
MinuteCounter2.prototype.calculate=function(){
    var secDiff = Math.round(((new Date()) - this.beginDate)/1000);
    var nextUpdate = 86400 - (secDiff % 86400);
    var tmp = (tmp = secDiff/60) < 1? 0 : Math.floor(tmp);
    var days = (tmp < 10 ? ("00" + tmp) : tmp < 100 ? ("0" + tmp) : tmp);
    this.container.innerHTML = 
        "= <strong>" + days + "</strong> " + (days == 1? "day" : "Minuten");
    var self = this;
    setTimeout(function(){self.calculate();}, (++nextUpdate*1000));
}

window.onload=function(){ 
	new DayCounter1('June 3, 2007 5:00:00', 'daycounter1');
	new HourCounter1('June 3, 2007 5:00:00', 'hourcounter1');
	new MinuteCounter1('June 3, 2007 5:00:00', 'minutecounter1');
	new DayCounter2('July 18, 2012 19:00:00', 'daycounter2');
	new HourCounter2('July 18, 2012 19:00:00', 'hourcounter2');
	new MinuteCounter2('July 18, 2012 19:00:00', 'minutecounter2');
	 
};