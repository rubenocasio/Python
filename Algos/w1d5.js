function zipArraysIntoMap(keys, values) {
    
    // The 'reduce' method is called on the 'keys' array.
    // It takes a callback function and an initial value (empty object {}) as its arguments.
    return keys.reduce((acc, key, idx) => {
        
        // Inside the callback:
        // 'acc' is the accumulator object that will eventually hold the final key-value pairs.
        // 'key' is the current key being processed in the 'keys' array.
        // 'idx' is the current index of the 'key' in the 'keys' array.

        // Check if the current index 'idx' is within the bounds of the 'values' array.
        // This ensures that we don't try to access an undefined value if the 'keys' array is longer than the 'values' array.
        if (idx < values.length) {

            // If the condition is true, add a new key-value pair to the 'acc' object.
            // The key is the current 'key' from the 'keys' array, and the value is the corresponding value from the 'values' array.
            acc[key] = values[idx];
        }

        // The 'acc' object is returned after processing each key. 
        // This allows 'reduce' to pass the updated 'acc' to the next iteration.
        return acc;

    // The initial value for the 'acc' object is an empty object ({}).
    }, {}); 
}

//Testing
console.log(zipArraysIntoMap(keys1, vals1));  // Expected output: { abc: 42, 3: 'wassup', yo: true }
console.log(zipArraysIntoMap(keys2, vals2));  // Expected output: {}
console.log(zipArraysIntoMap(keys3, vals3));  // Expected output with the provided test cases