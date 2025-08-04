const KEY_LENGTH = 100;
const START_CODE = 97;
const END_CODE = 122;
const NUMBER_OF_CHARS = END_CODE - START_CODE + 1;

class SimpleCipher {
  private keys: number[];

  constructor(public key: string = SimpleCipher.randomKey) {
    if (!/^[a-z]+$/.test(key)) {
      throw new Error("Bad key");
    }
    this.keys = SimpleCipher.generateArrayKeys(this.key);
  }

  private static get randomCharCode(): number {
    return Math.floor(Math.random() * NUMBER_OF_CHARS) + START_CODE;
  }

  private static get randomKey(): string {
    return Array(KEY_LENGTH)
      .fill(0)
      .map(() => String.fromCharCode(SimpleCipher.randomCharCode))
      .join("");
  }

  private static generateArrayKeys(key: string): number[] {
    return [...key].map(char => char.charCodeAt(0) - START_CODE);
  }

  private getKeyCharCode(index: number): number {
    return this.keys[index % this.keys.length];
  }

  private getCipheredCharCode(charCode: number, keyCharCode: number): number {
    return charCode - START_CODE + keyCharCode;
  }

  private getCipherCharCode(charCode: number, index: number): number {
    return (
      (this.getCipheredCharCode(charCode, this.getKeyCharCode(index)) %
        NUMBER_OF_CHARS) +
      START_CODE
    );
  }

  private getDecodedCharCode(charCode: number, index: number): number {
    const tempCode = this.getCipheredCharCode(
      charCode,
      -this.getKeyCharCode(index),
    );
    return tempCode < 0 ? END_CODE + tempCode + 1 : tempCode + START_CODE;
  }

  private static transform(
    text: string,
    fn: (charCode: number, index: number) => number,
  ): string {
    return [...text]
      .map((char, index) => String.fromCharCode(fn(char.charCodeAt(0), index)))
      .join("");
  }

  encode(message: string) {
    return SimpleCipher.transform(message, this.getCipherCharCode.bind(this));
  }

  decode(message: string) {
    return SimpleCipher.transform(message, this.getDecodedCharCode.bind(this));
  }
}

export default SimpleCipher;
