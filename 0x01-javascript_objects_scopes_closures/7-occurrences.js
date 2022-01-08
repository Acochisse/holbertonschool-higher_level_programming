#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let theCounter = 0;
    for (let i = 0; i < list.length; i++) {
      if (list[i] === searchElement) {
        theCounter++;
      }
    }
    return (theCounter);
  };
