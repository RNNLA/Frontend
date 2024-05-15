
<script lang="ts">
    import { onMount, afterUpdate } from 'svelte';
    import * as d3 from 'd3';

    import {graphDataModels} from '../store'

    let svg_width:number = 700;
    let svg_height:number = 350;

    const legend_height:number = 70;
    const margin = { top: 10, right: 50, bottom: 75+legend_height, left: 60 };

    let width:number = svg_width - margin.left - margin.right;
    let height:number = svg_height - margin.top - margin.bottom;

    const colors = ["var(--positive-color)", "var(--negative-color)"];

      

    function create_chart () {
      let data = JSON.parse(JSON.stringify($graphDataModels));

      let keys = ['positive_count', 'negative_count'];
      let stacked_data = d3.stack().keys(keys)(data);

      let x = d3.scaleBand().range([0, width]).domain(data.map(d => d.timestamp)).padding(0.2);
      let y = d3.scaleLinear().range([height, 0]).domain([0, Math.max.apply(null, data.map(wordObj => wordObj.positive_count + wordObj.negative_count))]);
      let svg = d3.select("#chart")
              .append("div")
              .classed("container", true)
              .append("svg")
              .attr("viewBox", `0 0 700 380`)
              .attr("preserveAspectRatio", "xMinYMin meet")
              .classed("svg-content",true)

      let chart = d3.select(".svg-content")
                    .append("g")
                    .attr("transform", `translate(${margin.left},${margin.top})`)
                    .classed("chart", true)
        
      // x axis
      chart.append('g')
          .attr('transform', `translate(0,${height})`)
          .call(d3.axisBottom(x))
          .classed('x_axis', true);

      chart.select('.x_axis')
          .attr("text-anchor", "end")
          .selectAll("text")
          .attr("font-weight", "500")
          .attr("font-size", "1.25rem")
          .attr("color", "var(--highlight-color)")
          .attr("transform", "rotate(-65)")
          .attr("dy", "0.3em")
          .attr("dx", "-0.5em")
      
      // y axis
      chart.append('g')
          .call(d3.axisLeft(y).tickFormat((d)=>d))
          .classed('y_axis', true);

      chart.select('.y_axis')
            .selectAll('text')
            .attr("font-size", "1.25rem")
            .attr("color", "var(--highlight-color)")
      
      // drawing layers
      const layers = chart.selectAll('.layer')
                        .data(stacked_data)
                        .enter()
                        .append('g')
                        .classed('layer', true)
                        .style('fill', (d,i) => colors[i])
                          .selectAll('rect')
                          .data(d => d)
                          .enter()
                          .append('rect')
                          .attr('y', d => y(d[1]))
                          .attr('x', d => x(d.data.timestamp))
                          .attr('width', x.bandwidth())
                          .attr('height', d => {
                            return y(d[0]) - y(d[1]);
                          })
                          .classed("bar", true)
                          .on("mouseover", onMouseOver)
                          .on("mouseout", onMouseOut);
          
          // legend
          let legend = d3.select(".svg-content")
                          .append("g")
                          .attr("transform", `translate(${width/2 - 10},${height + 150})`)
                          .classed("legend", true)

          const legend_width_control_var = 5;
          const legend_width_rect_text_interval = 35;
          const legend_height_control_var = -15;
          const legend_height_rect_text_interval = 4;
          const legend_height_positive_negative_interval = 29;
          
          const legend_positive_box = legend.append('rect')
                                        .attr("width", "1.3rem")
                                        .attr("height", "1.3rem")
                                        .attr("x", legend_width_control_var)
                                        .attr("y", legend_height_control_var)
                                        .style("fill", "var(--negative-color)")
                                        
          const legend_positive_text = legend.append('text')
                                            .text("부정 기사")
                                            .attr("x", legend_width_rect_text_interval)
                                            .attr("y", legend_height_rect_text_interval)
                                            .attr("font-weight", "600")
                                            .attr("font-size", "1.3rem")
                                            .style("fill", "var(--negative-color)")

          const legend_negative_box = legend.append('rect')
                                          .attr("width", "1.3rem")
                                          .attr("height", "1.3rem")
                                          .attr("x", legend_width_control_var)
                                          .attr("y", legend_height_control_var + legend_height_positive_negative_interval)
                                          .style("fill", "var(--positive-color)")
                                        
          const legend_negative_text = legend.append('text')
                                            .text("긍정 기사")
                                            .attr("x", legend_width_rect_text_interval)
                                            .attr("y", legend_height_rect_text_interval + legend_height_positive_negative_interval)
                                            .attr("font-weight", "600")
                                            .attr("font-size", "1.3rem")
                                            .style("fill", "var(--positive-color)")
          
          function onMouseOver(event, d){
            const self = event.target;
            let color = "";
            let popup_box_manual_x = 50;
            let popup_box_manual_x_for_last = popup_box_manual_x * 3;
            d3.select(self)
              .style("fill", ()=>{
                color = (d[0] == 0 ? "#4F641A" : "#691A16");
                return color;
              })

            const text = d3.select(".chart")
                          .append("g")
                          .attr("id", "popup_box")
          
            text.append("rect")
                .attr("x",() => x(d3.select(self).datum().data.timestamp) - x.bandwidth()/2+popup_box_manual_x)
                .attr("y",() => y(d3.select(self).datum()[1]) + (y(d3.select(self).datum()[0]) - y(d3.select(self).datum()[1]))/3)
                .attr("rx", 20)
                .attr("ry", 20)
                .attr("width", "10em")
                .attr("height", "4em")
                .classed("popup_rect",true)
                .style("z-index", "-1")
                .style("stroke-width", "3px")
                .style("stroke",color)
                .style('fill', "white")

              
            text.append("text")
                .attr("x",() => x(d3.select(self).datum().data.timestamp) - x.bandwidth()/2+20+popup_box_manual_x)
                .attr("y",() => y(d3.select(self).datum()[1]) + (y(d3.select(self).datum()[0]) - y(d3.select(self).datum()[1]))/3+50)
                .attr("id", "popup_box")
                .text("긍정 기사 : ")
                .attr("font-weight", "500")
                .style("fill", "#98C039")
                .classed("popup_positive_text", true)
                .append("tspan")
                .text(`${d3.select(self).datum().data.positive_count}`)
                .attr("font-weight", "700")
                .attr("color", "#98C039")
                .append("tspan")
                .text("건")
                .attr("font-weight", "500")
                .attr("color", "#98C039")
                  
            text.append("text")
                .attr("x",() => x(d3.select(self).datum().data.timestamp) - x.bandwidth()/2+20+popup_box_manual_x)
                .attr("y",() => y(d3.select(self).datum()[1]) + (y(d3.select(self).datum()[0]) - y(d3.select(self).datum()[1]))/3+25)
                .attr("id", "popup_box")
                .classed("popup_negative_text", true)
                .text("부정 기사 : ")
                .attr("font-weight", "500")
                .style("fill", "#D43C36")
                .append("tspan")
                .text(`${d3.select(self).datum().data.negative_count}`)
                .attr("font-weight", "700")
                .append("tspan")
                .text("건")
                .attr("font-weight", "500")
              
            const rects_one = document.querySelector("#chart > div > svg > g > g:nth-child(3)")?.children;
            const rects_two = document.querySelector("#chart > div > svg > g > g:nth-child(4)")?.children;
            
            // for (let rect = 0; rect < rects_cnt)
            for (let index = 0; index < rects_one.length; index++) {
                    const element = rects_one[index];
                    if ((rects_one.length - (index)) <= 6 && element === self) {
                      d3.selectAll('.popup_rect')
                        .attr("x", `${self.getAttribute("x") - popup_box_manual_x_for_last - 20}`);
                      d3.selectAll('.popup_positive_text')
                        .attr("x", `${self.getAttribute("x") - popup_box_manual_x_for_last}`);
                      d3.selectAll('.popup_negative_text')
                        .attr("x", `${self.getAttribute("x") - popup_box_manual_x_for_last}`);
                    } 
                    
                  }

            for (let index = 0; index < rects_two.length; index++) {
                    const element = rects_two[index];
                    if ((rects_two.length - (index)) <= 6 && element === self) {
                      d3.selectAll('.popup_rect')
                        .attr("x", `${self.getAttribute("x") - popup_box_manual_x_for_last - 20}`);
                      d3.selectAll('.popup_positive_text')
                        .attr("x", `${self.getAttribute("x") - popup_box_manual_x_for_last}`);
                      d3.selectAll('.popup_negative_text')
                        .attr("x", `${self.getAttribute("x") - popup_box_manual_x_for_last}`);
                    } 
                    
                  }
          }

          function onMouseOut(event, d){
            const self = event.target;
            d3.select(self)
              .style("fill", ()=>{
                return d[0] == 0 ? "#98C039" : "#D43C36";
                
              });
            
              d3.selectAll('#popup_box')
                .remove();
          }
        }
    
      
        
        
        
      
    
      
    afterUpdate(() => {
      
    })
    

    onMount(() => {
      create_chart();
      })

    

</script>
  
  <!-- 차트를 표시할 요소 -->
  <div id="chart"></div>

  <style>
  </style>


