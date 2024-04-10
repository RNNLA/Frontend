<script lang='ts'>
    import { listenArrayEvents } from 'chart.js/helpers';
import * as d3 from 'd3';
import cloud from 'd3-cloud';
import { onMount, afterUpdate} from 'svelte';

let width:number = 900;
let height:number = 450;
let margin = {top: 10, right: 10, bottom: 10, left: 10};

const myWords = [
    { word: "Word0", size: 262159, is_not_risk: true },
    { word: "Word1", size: 129618, is_not_risk: true },
    { word: "Word2", size: 59773, is_not_risk: false },
    { word: "Word3", size: 57590, is_not_risk: true },
    { word: "Word4", size: 53225, is_not_risk: true },
    { word: "Word5", size: 52912, is_not_risk: false },
    { word: "Word6", size: 52471, is_not_risk: true },
    { word: "Word7", size: 48088, is_not_risk: true },
    { word: "Word8", size: 43134, is_not_risk: false },
    { word: "Word9", size: 41432, is_not_risk: true },
    { word: "Word10", size: 40385, is_not_risk: false },
    { word: "Word11", size: 39703, is_not_risk: true },
    { word: "Word12", size: 39614, is_not_risk: true },
    { word: "Word13", size: 39561, is_not_risk: true },
    { word: "Word14", size: 37342, is_not_risk: false },
    { word: "Word15", size: 36240, is_not_risk: true },
    { word: "Word16", size: 35687, is_not_risk: true },
    { word: "Word17", size: 35610, is_not_risk: false },
    { word: "Word18", size: 34745, is_not_risk: true },
    { word: "Word19", size: 32738, is_not_risk: true },
    { word: "Word20", size: 32505, is_not_risk: true },
    { word: "Word21", size: 31963, is_not_risk: true },
    { word: "Word22", size: 31526, is_not_risk: true },
    { word: "Word23", size: 30665, is_not_risk: true },
    { word: "Word24", size: 29916, is_not_risk: true },
    { word: "Word25", size: 29189, is_not_risk: true },
    { word: "Word26", size: 28528, is_not_risk: true },
    { word: "Word27", size: 28417, is_not_risk: false },
    { word: "Word28", size: 8990, is_not_risk: true },
    { word: "Word29", size: 938, is_not_risk: true },
    { word: "Word30", size: 703, is_not_risk: true },
    { word: "Word31", size: 99, is_not_risk: false },
    { word: "Word32", size: 20, is_not_risk: true },
    { word: "Word33", size: 445, is_not_risk: true },
    { word: "Word34", size: 184, is_not_risk: false },
    { word: "Word35", size: 742, is_not_risk: true },
    { word: "Word36", size: 99, is_not_risk: true },
    { word: "Word37", size: 71, is_not_risk: false },
];

let wordSorted = myWords.sort((a, b) => b.size - a.size);
wordSorted = wordSorted.slice(0, 30);

afterUpdate(async()=>{
        // set the dimensions and margins of the graph
        
		const cloudDiv = document.querySelector('#cloud');
		width = cloudDiv?.parentElement?.offsetWidth??width;
		height = cloudDiv?.parentElement?.offsetHeight??height;

		cloudDiv?.firstElementChild?.setAttribute("width", (width).toString());
		cloudDiv?.firstElementChild?.setAttribute("height", height.toString());
});

onMount(()=>{
    // append the svg object to the body of the page
    var svg = d3.select("#cloud").append("svg")
                    .attr("width", width + margin.left + margin.right)
                    .attr("height", height + margin.top + margin.bottom)
                .append("g")
                    .attr("transform",
                        "translate(" + margin.left + "," + margin.top + ")");


    const sizeScale = d3.scaleLinear()
                .range([10, 80])
                .domain([1, Math.max.apply(null, myWords.map(wordObj => wordObj.size))])

    // Constructs a new cloud layout instance. It run an algorithm to find the position of words that suits your requirements
    // Wordcloud features that are different from one word to the other must be here
    var layout = cloud()
                .size([width, height])
                .words(wordSorted.map(function(d) { return {text: d.word, size:d.size, is_not_risk:d.is_not_risk}; }))
                .padding(10)        //space between words
                .rotate(function() { return ~~(Math.random() * 2) * 90; })
                .fontSize(function(d) { return sizeScale(d.size); })      // font size of words
                .on("end", draw);
    layout.start();


    // This function takes the output of 'layout' above and draw the words
    // Wordcloud features that are THE SAME from one word to the other can be here
    function draw(words) {
        svg.append("g")
            .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
            .attr("id", "cloud_content")
            .selectAll("text")
                .data(words)
            .enter().append("text")
                .style("font-size", function(d) { return d.size; })
                .style("fill", d => {
                    console.log(d);
                    return d.is_not_risk ? "var(--positive-color)" : "var(--negative-color)"})
                .attr("text-anchor", "middle")
                .style("font-family", "Impact")
                .attr("transform", function(d) {
                return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .text(function(d) { return d.text; });
        
        }
    
});


    
</script>
<div id="cloud"></div>



<style>
    div {
        justify-content: center;
        display: flex;
    }
</style>