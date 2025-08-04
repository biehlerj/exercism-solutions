class Squares {
  initialValue: number;
  result1: number = 0;
  result2: number = 0;
  squareOfSum: number;
  sumOfSquares: number;
  difference: number;

  constructor(squares: number) {
    for (let i = 0; i <= squares; i++) {
      this.result1 += i;
    }
    this.squareOfSum = this.result1 * this.result1;

    for (let i = 0; i<= squares; i++) {
      this.result2 += i * i;
    }
    this.sumOfSquares = this.result2;
    this.difference = this.squareOfSum - this.sumOfSquares;
  }
}

export default Squares;