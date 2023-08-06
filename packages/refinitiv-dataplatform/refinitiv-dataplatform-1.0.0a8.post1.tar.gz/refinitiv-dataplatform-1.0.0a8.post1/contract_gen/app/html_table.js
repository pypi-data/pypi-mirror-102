var trs = document.getElementsByTagName('table')[1].getElementsByTagName('tr')
var s = "";
var prior = 100 + trs.length;
for (let item of trs) {
    prior -= 1;
    var value = item.getElementsByTagName('td')[0].innerText;
    s += `\n"${value}": ${prior},`;
}
s += '\n'
console.log(s)