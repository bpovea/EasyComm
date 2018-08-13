//views
var FaqsView = Backbone.View.extend({
  // el:"#faqs-here",
  el: "#accordion",
  render: function(){
    var that = this;
    faqs.fetch({
      success: function(faqs){
        var template = _.template($('#faq_template').html());
        that.$el.html(template({
          faqs:faqs.models
        }));
      },
      error: function(vehicles, response){
        hideloader();
        createalert("Error, No se pueden cargar las FAQs.");
      }
    });
  },
  events: {
    "click .faq":"sayHello",
  },
  sayHello: function(ev){
    console.log('hello')
  }
});
