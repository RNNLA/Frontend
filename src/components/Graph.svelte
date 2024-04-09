
<script lang="ts">
    import { onMount, afterUpdate } from 'svelte';
    import * as d3 from 'd3';
  
    // 예시 데이터
    let data = [
      {date: '24-03-20',positive: 40, negative: 60, positive_data: 100, negative_data: 200},
      {date: '24-03-21',positive: 30, negative: 70, positive_data: 100, negative_data: 200},
      {date: '24-03-22',positive: 50, negative: 50, positive_data: 100, negative_data: 200},
      {date: '24-03-23',positive: 20, negative: 80, positive_data: 100, negative_data: 200},
      {date: '24-03-24',positive: 60, negative: 40, positive_data: 100, negative_data: 200},
      {date: '24-03-25',positive: 70, negative: 30, positive_data: 100, negative_data: 200},
      {date: '24-03-26',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-03-27',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-03-28',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-03-29',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-03-30',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-03-31',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-01',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-02',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-03',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-04',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-05',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-06',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      {date: '24-04-07',positive: 80, negative: 20, positive_data: 100, negative_data: 200},
      // {date: '24-03-26',positive: 80, negative: 20},
      // {date: '24-03-26',positive: 80, negative: 20},
      // {date: '24-03-26',positive: 80, negative: 20},
      // {date: '24-03-26',positive: 80, negative: 20},
      // {date: '24-03-26',positive: 80, negative: 20},
      // {date: '24-03-26',positive: 80, negative: 20},
    ];

    let svg_width:number = 400;
    let svg_height:number = 300;
    
    const margin = { top: 10, right: 30, bottom: 70, left: 40 };

    function createChart(){
        const colors = ["#98C039", "#D43C36"];
        const width:number = svg_width - margin.left - margin.right;
        const height:number = svg_height - margin.top - margin.bottom;

        const svg = d3.select('#chart')
                    .append('svg')
                    .attr('width', svg_width)
                    .attr('hieght', svg_height)
                    .attr('viewBox', `0 0 ${svg_width} ${svg_height}`)

        const chart = svg.append('g')
                    .attr('transform', `translate(${margin.left},${margin.top})`)
                    .classed("chart_content", true);

        const x = d3.scaleBand().range([0, width]).domain(data.map(d => d.date)).padding(0.2);
        const y = d3.scaleLinear().range([height, 0]).domain([0, 100]);

        const keys = ['positive', 'negative'];
        const stacked_data = d3.stack().keys(keys)(data);

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
            .attr("transform", "rotate(-45)")
            .attr("dy", "1.5em")
            .attr("dx", "1em")
        
        // y axis
        chart.append('g')
            .call(d3.axisLeft(y))
            .classed('y_axis', true);

        chart.select('.y_axis')
              .selectAll('text')
              .attr("font-size", "1.25rem")
              .attr("color", "var(--highlight-color)")

        
        // Drawing Chart
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
                          .attr('x', d => x(d.data.date))
                          .attr('width', x.bandwidth())
                          .attr('height', d => y(d[0]) - y(d[1]))
                          .classed("bar", true)
                          .on("mouseover", onMouseOver)
                          .on("mouseout", onMouseOut);

        function onMouseOver(event, d){
          const self = event.target;
          let color = "";
          let popup_box_manual_x = 60;
          let popup_box_manual_x_for_last = popup_box_manual_x * 2.25;
          d3.select(self)
            .style("fill", ()=>{
              color = (d[0] == 0 ? "#4F641A" : "#691A16");
              return color;
            })

          const text = chart.append('g')
                            .attr("id", "popup_box")
                            
          const rects_one = document.querySelector("#chart > svg > g > g:nth-child(3)")?.children;
          const rects_two = document.querySelector("#chart > svg > g > g:nth-child(4)")?.children;
        
          
          text.append("rect")
              .attr("x",() => x(d3.select(self).datum().data.date) - x.bandwidth()/2+popup_box_manual_x)
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
                .attr("x",() => x(d3.select(self).datum().data.date) - x.bandwidth()/2+20+popup_box_manual_x)
                .attr("y",() => y(d3.select(self).datum()[1]) + (y(d3.select(self).datum()[0]) - y(d3.select(self).datum()[1]))/3+25)
                .attr("id", "popup_box")
                .text("긍정 기사 : ")
                .attr("font-weight", "500")
                .style("fill", "#98C039")
                .classed("popup_positive_text", true)
                .append("tspan")
                .text(`${d3.select(self).datum().data.positive_data}`)
                .attr("font-weight", "700")
                .attr("color", "#98C039")
                .append("tspan")
                .text("건")
                .attr("font-weight", "500")
                .attr("color", "#98C039")
                
                text.append("text")
                .attr("x",() => x(d3.select(self).datum().data.date) - x.bandwidth()/2+20+popup_box_manual_x)
                .attr("y",() => y(d3.select(self).datum()[1]) + (y(d3.select(self).datum()[0]) - y(d3.select(self).datum()[1]))/3+50)
                .attr("id", "popup_box")
                .classed("popup_negative_text", true)
                .text("부정 기사 : ")
                .attr("font-weight", "500")
                .style("fill", "#D43C36")
                .append("tspan")
                .text(`${d3.select(self).datum().data.negative_data}`)
                .attr("font-weight", "700")
                .append("tspan")
                .text("건")
                .attr("font-weight", "500")

                for (let index = 0; index < rects_one.length; index++) {
                  const element = rects_one[index];
                  if ((rects_one.length - (index)) <= 3 && element === self) {
                    console.log(self.getAttribute("x"));
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
                  if ((rects_two.length - (index)) <= 3 && element === self) {
                    console.log(self.getAttribute("x"));
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
              return d[1] != 100 ? "#98C039" : "#D43C36";
              
            });
          
            d3.selectAll('#popup_box')
              .remove();
        }

      }


    afterUpdate(()=>{
        // set the dimensions and margins of the graph
        
      const chartDiv = document.querySelector('#chart');
      svg_width = chartDiv?.parentElement?.clientWidth??svg_width - margin.left - margin.right;
      svg_height = chartDiv?.parentElement?.clientHeight??svg_height - margin.top - margin.bottom;
      
      chartDiv?.firstElementChild?.setAttribute("width", svg_width.toString());
		  chartDiv?.firstElementChild?.setAttribute("height", svg_height.toString());

      d3.select('svg')
        .remove()

      createChart();
      console.log(chartDiv?.firstElementChild);
  });

    


    onMount(() => {
      createChart();
    });
</script>
  
  <!-- 차트를 표시할 요소 -->
  <div id="chart">
  </div>

  <style>
  </style>


