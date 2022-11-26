#!/usr/bin/node

const Squarez = require('./5-square');

module.exports = class Square extends Squarez {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
      }
    } else {
      this.print();
    }
  }
};
