import { expect } from "chai";
import { PalindromeKata } from "../src/index";

describe("PalindromeKata", () => {
  let palindromeKata: PalindromeKata;

  beforeEach(function () {
    palindromeKata = new PalindromeKata();
  });

  it("isPalindrome method should check if parameter is a palindrome", () => {
    expect(palindromeKata.isPalindrome("abba")).to.be.true;
  });

  it("isPalindrome method should be case insensitive", () => {
    expect(palindromeKata.isPalindrome("Racecar")).to.be.true;
  });

  it("should return false if myString is not a palindrome", () => {
    expect(palindromeKata.isPalindrome("hello")).to.be.false;
  });
});
