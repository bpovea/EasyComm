
function incrementar(){
    $("#qty").val(parseInt($("#qty").val())+1)
}

function decrementar(){
    if(parseInt($("qty").val()) > 1){
        $("#qty").val(parseInt($("#qty").val())-1)
    }
    else{
        createalert('Minimo es 1 producto')
    }
}

function renderGraph(json){
	var config = { columnWidth: 35, columnHeight: 250, columnGap: 10, padding: 80};
    var datos = json[0].ventas;
    
    var NUM_COLUMNAS = datos.length;
    config.width = NUM_COLUMNAS * (config.columnWidth + config.columnGap) + (2 * config.padding);
    config.height = config.columnHeight + 2 * config.padding;
    var unidades_vendidas_max = d3.max(datos, function(d) { return +d.unidadesVendidas; });
    
    var x = d3.scaleBand()
        .range([0, config.width - 2 * config.padding])
        .domain(datos.map(function(d) { return d.mes; }));
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
            return "<strong>" + d.mes + "</strong><br> Unidades vendidas: " +d.unidadesVendidas;
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
        .attr("x", function(d,i) { return config.padding + x(d.mes) })
        .attr("y", function(d,i) { return config.padding + config.columnHeight - y(d.unidadesVendidas) })
        .attr("height", function(d,i) { return y(d.unidadesVendidas) })
            .on('mouseover', tooltip.show)
            .on('mouseout', tooltip.hide)
}

$(document).ready(function(){
	var oldsrc;
	$('#mini-img > img').mouseenter(function(ev){
		oldsrc = $('#main-img').attr('src')
		$('#main-img').attr('src',$(ev.currentTarget).attr('src'))
	}).mouseleave(function(ev){
		$('#main-img').attr('src',oldsrc)
	})

	$('#mini-img > img').click(function (ev) {
		oldsrc = $(ev.currentTarget).attr('src')
		$('#main-img').attr('src',$(ev.currentTarget).attr('src'))
	})

	$('#mini-img-mobile > img').mouseenter(function(ev){
		oldsrc = $('#main-img').attr('src')
		$('#main-img').attr('src',$(ev.currentTarget).attr('src'))
	}).mouseleave(function(ev){
		$('#main-img').attr('src',oldsrc)
	})

	$('#mini-img-mobile > img').click(function (ev) {
		oldsrc = $(ev.currentTarget).attr('src')
		$('#main-img').attr('src',$(ev.currentTarget).attr('src'))
	})


	/* grafico estadistico */
	$.ajax({
        url: "data/products.json",
        type:"GET",    
        dataType : 'json',
        success : renderGraph,
        error : function(xhr, status) {
            alert('Disculpe, existió un problema al cargar los datos del producto.');
        }
    });
	
});
