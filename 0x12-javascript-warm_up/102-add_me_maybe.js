#!/usr/bin/node
// a function that increment and calls theFunction


exports.addMeMaybe = function (number, theFunction) {
    theFunction(++number);
};
