export class PalindromeKata {
  isPalindrome(myString: string) {
    const split = myString.toLowerCase().split("", myString.length);
    const reverse = myString.toLowerCase().split("", myString.length).reverse();

    if (split.length && reverse.length) {
      if (split.every((val, i) => val === reverse[i])) {
        return true;
      }
      return false;
    }
    return false;
  }
}
