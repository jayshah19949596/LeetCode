/*
2667. Create Hello World Function
https://leetcode.com/problems/create-hello-world-function

### 1. Question Explanation:
----------------------------
Write a function createHelloWorld. It should return a new function that always returns "Hello World".
*/

function createHelloWorld() {

    function getHelloWorld(...args): string {
        return "Hello World"
    };
    return getHelloWorld
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */