import { expect } from "chai";
import { summation } from "summationKata";

describe("summation kata test", () => {
  it("should return sum of 1 to num", () => {
    expect(summation(1)).equals(1);
    expect(summation(5)).equals(15);
    expect(summation(8)).equals(36);
  });
});
