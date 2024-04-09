<script lang='ts'>
import * as d3 from 'd3';
import cloud from 'd3-cloud';
import { onMount, afterUpdate} from 'svelte';

let width:number = 900;
let height:number = 450;
let margin = {top: 10, right: 10, bottom: 10, left: 10};

const myWords = [
    {word: "반도체", size: 100, is_not_risk: true},
    {word: "삼성", size:200, is_not_risk: true},
    {word: "금", size:50, is_not_risk: false},
    {word: "SK머터리얼즈", size:50, is_not_risk: true}
];

afterUpdate(async()=>{
        // set the dimensions and margins of the graph
        
		const cloudDiv = document.querySelector('#cloud');
		width = cloudDiv?.parentElement?.offsetWidth??width - margin.left - margin.right;
		height = cloudDiv?.parentElement?.offsetHeight??height - margin.top - margin.bottom;

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

    // Constructs a new cloud layout instance. It run an algorithm to find the position of words that suits your requirements
    // Wordcloud features that are different from one word to the other must be here
    var layout = cloud()
                .size([width, height])
                .words(myWords.map(function(d) { return {text: d.word, size:d.size, is_not_risk:d.is_not_risk}; }))
                .padding(5)        //space between words
                .rotate(function() { return ~~(Math.random() * 2) * 90; })
                .fontSize(function(d) { return d.size; })      // font size of words
                .on("end", draw);
    layout.start();

    // This function takes the output of 'layout' above and draw the words
    // Wordcloud features that are THE SAME from one word to the other can be here
    function draw(words) {
        svg.append("g")
            .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
            .selectAll("text")
                .data(words)
            .enter().append("text")
                .style("font-size", function(d) { return d.size; })
                .style("fill", d => {return d.is_not_risk ? "var(--positive-color)" : "var(--negative-color)"})
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

<svelte:window on:load="{()=>handleonload()}"/>