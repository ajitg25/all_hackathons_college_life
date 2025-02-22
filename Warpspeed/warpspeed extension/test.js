
const sample = require('./sample.json');

htlevel = ""
htchild = ""
let level = 0;

for (const key in sample) {
    htlevel += "<div id=\"elem"+level+"\" class=\"level1 elem\">"+key+"</div>"
    if (sample.hasOwnProperty(key)) {
        let len = sample[key].length>2?2:sample[key].length;
        for(let i = 0;i<len;i++){
            htchild += "<div id=\"elem"+(level)+"child"+(i)+"\" class=\"elem elem"+(level)+"child level2"+"\">"+sample[key][i].title +" \n "+ "<a href=" + sample[key][i].video_link + "></a></div>"
        }
    }
    level++;
  }

ht = htlevel + htchild
console.log(ht)