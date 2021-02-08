#!/usr/bin/node
// Script that converts DEC

exports.converter = function (base) {
    return function (num) {
	return num.toString(base);
    };
};
