function renderGraph(datos,unidades){
    $("#graph").html("");
    var config = { columnWidth: 50, columnHeight: 250, columnGap: 50, padding: 80};
    var NUM_COLUMNAS = datos.length;
    config.width = NUM_COLUMNAS * (config.columnWidth + config.columnGap) + (2 * config.padding);
    config.height = config.columnHeight + 2 * config.padding;
    var unidades_vendidas_max = d3.max(datos, function(d) { return +d.valor; });
    
    var x = d3.scaleBand()
        .range([0, config.width - 2 * config.padding])
        .domain(datos.map(function(d) { return d.nombre; }));
    var y = d3.scaleLinear()
        .range([0, config.columnHeight])
        .domain([0, unidades_vendidas_max]);
    var rangeY = d3.scaleLinear()
        .range([config.columnHeight, 0])
        .domain([0, unidades_vendidas_max]);
    var ejeX = d3.axisTop().scale(x);
    var ejeY = d3.axisLeft().scale(rangeY);
    var tooltip = d3.tip()
        .attr('class', 'barraMensaje')
        .html(function(d) {
            return "<strong>" + d.nombre + "</strong><br> " + unidades + ":"+d.valor;
        });
    var svg = d3.select("svg")
        .attr("width", config.width)
        .attr("height", config.height);
    svg.call(tooltip);
    svg.append("g")
        .attr("class", "eje")
        .attr("transform", "translate(" + config.padding + "," + (10 + config.padding + config.columnHeight) + ")")
        .call(ejeX)
      .selectAll("text")
        .attr("transform", "rotate(90)")
        .style("text-anchor", "start");
    svg.append("g")
        .attr("class", "eje")
        .attr("transform", "translate(" + (config.padding - 10) + "," + config.padding + ")")
        .call(ejeY);
    svg.selectAll("rect")
        .data(datos)
        .enter().append("rect")
        .attr("width", config.columnWidth)
        .attr("x", function(d,i) { return config.padding + x(d.nombre) })
        .attr("y", function(d,i) { return config.padding + config.columnHeight - y(d.valor) })
        .attr("height", function(d,i) { return y(d.valor) })
            .on('mouseover', tooltip.show)
            .on('mouseout', tooltip.hide)
}