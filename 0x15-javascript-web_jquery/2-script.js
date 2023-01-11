#!/usr/bin/node

const header = $('header');
$('div#red_header').on('click', function (event) {
  header.attr('color', '#FF0000');
});
