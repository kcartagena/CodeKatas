export const summation = (num:number)=> { 
    let total = 0;
    let myNumContainer =[];
    if(num){
      for(let i = 0; i <= num; i++ ){
        myNumContainer.push(i);
        total += myNumContainer[i];
      }
      return total;
    }
    throw new Error('The method or operation is not implemented.')
  }