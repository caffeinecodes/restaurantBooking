$.fn.serializeObject = function()
{
   var o = {};
   var a = this.serializeArray();
   $.each(a, function() {
       if (o[this.name]) {
           if (!o[this.name].push) {
               o[this.name] = [o[this.name]];
           }
           o[this.name].push(this.value.trim() || '');
       } else {
           o[this.name] = this.value.trim() || '';
       }
   });
   return o;
};

String.prototype.toProperCase = function () {
    return this.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
};

$(document).ready(function(){
    ajaxFactory.ajaxHandler("/api/categories/", "GET", {}, function (response) {
        if (response.code == 200) {
            var template = _.template($('#categoryTemplate').html());
            var innerHtml = template({categories: response.data.categories});
            $('#categoryList').html(innerHtml).select2();
            $("#listCategory").append(innerHtml).select2();
        }
    });
    $("#addItemForm").submit(function (e) {
        e.preventDefault();
    });
    
    $("#addItemForm").validate({
        ignore: [],
        onblur: function (element) {
            $(element).valid();
        },
        rules: {
            name: {
                required: true
            },
            category:{
                required: true
            },
            mrp:{
                required: true,
                min: 1
            },
            offer_price:{
                required: true,
                min: 1
            },
            description:{
                required: true,
            }
        },
        messages: {
            name: "Please enter the menu name!",
            category:"Please select the category",
            mrp: "Please enter the mrp price",
            offer_price: "Please enter the offer price",
            description: "Please enter the description"
        },
        submitHandler: function (form) {
            var post_data = $(form).serializeObject();
            post_data["is_veg"] = post_data["is_veg"] == "Veg" ? true :false;
            post_data["time_slot"] = JSON.stringify($("#timeSlots").val());
            ajaxFactory.ajaxHandler('/api/dishes/', 'POST', post_data, function (response) {
                // if (response.code == '900') {
                //     success_toast(response.message)
                // }
            });
    
        }
    });

    $(document).on("keyup","input.form-control[name='mrp']",function(){
        console.log($(this).val())
        $("input.form-control[name='offer_price']").val($(this).val())
    });
    $('#categoryList').select2();
    $("#timeSlots").select2();

    $("#timeSlots").on('change', function() {
        $(this).valid();
    });

    
})



