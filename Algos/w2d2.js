/* 
  Given a string,
  return a new string with the duplicate characters excluded
  Bonus: Keep only the last instance of each character.
*/
const str1 = "abcABCabcABCabcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

//bonus
const str5 = "aba"
const expected5 = "ba"

function stringDedupe(str) {
    //Logic goes here
}
console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));
console.log(stringDedupe(str5));

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const strA = "hello";
const expectedA = "olleh";

const strB = "hello world";
const expectedB = "olleh dlrow";

const strC = "abc def ghi";
const expectedC = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    //logic goes here
}
console.log(reverseWords(strA)) //expectedA: olleh
console.log(reverseWords(strB)) //expectedB: olleh dlrow
console.log(reverseWords(strC)) //expectedC: cba fed ihg



/*****************************************************************************/


















/**
* This function removes duplicate characters from a string.
* For characters that appear multiple times, only the last occurrence is retained.
* 
* @param {string} str - The input string that may contain duplicate characters.
* @returns {string} - The deduped string.
*/
function stringDedupe(str = "") {
    let distinctStr = "";
    const seen = {};
    for (let i = str.length - 1; i >= 0; --i) {
        if (!seen[str[i]]) {
            distinctStr = str[i] + distinctStr;
            seen[str[i]] = true;
        }
    }
    return distinctStr;
}

console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));
console.log(stringDedupe(str5));


function stringDedupe2(str) {
    let charPositions = {};

    for (let i = 0; i < str.length; i++) {
        charPositions[str[i]] = i;
    }
    return Object.keys(charPositions).sort((a, b) => charPositions[a] - charPositions[b]).join("");
}


function reverseWords(str) {
  let reversed = "";
  let temp = ""
  for (let char of str) {
    if (char === " ") {
      reversed += temp + " "
      temp = ""
    } else {
      temp = char + temp
    }
  }
  //capture last word
  reversed += temp;
  return reversed
}

console.log(reverseWords(strA)) //expectedA: olleh
console.log(reverseWords(strB)) //expectedB: olleh dlrow
console.log(reverseWords(strC)) //expectedC: cba fed ihg