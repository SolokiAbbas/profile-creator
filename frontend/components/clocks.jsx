import React from 'react';

class Clocks extends React.Component{

  constructor(){
    super();
    this.state={
     hours: 0,
     minutes: 0,
     seconds: 0
   };
   this.checkTime = this.checkTime.bind(this);
   this.startTime = this.startTime.bind(this);
  }
  render(){
    return(
      <div className="clock" onClick={()=>this.startTime()}>
        <h2>"Clock"</h2>
        <li>{this.state.hours}</li>
        <li>{this.state.minutes}</li>
        <li>{this.state.seconds}</li>
      </div>
    );
  }

  checkTime(i) {
    if (i < 10)
    i = "0" + i;
    return i;
  }

  startTime(){
    let today = new Date();
    this.setState({
      hours: today.getHours(),
      minutes: today.getMinutes(),
      seconds: today.getSeconds()
    });
    let t = setTimeout(this.startTime(), 500);
    }
  }

export default Clocks;
