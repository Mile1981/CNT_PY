
var APIKEY = "123";
var AUTHORIZATION = "ABC";
var hash = location.hash.substr(1);
var FULL_LAYOUT = "#full-layout"
var menu_list = $('#main-menu-navigation').find(' > li');

$(document).ready(function () {
    $('.loader').css('display','block');
  
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {

            xhr.setRequestHeader("X-Api-Key", APIKEY);
            xhr.setRequestHeader("Authorization", AUTHORIZATION);
        }
    });
    loadMenu();
    goURL(hash)

});


function onActive(element){
    console.log("MENU!!");
        console.log(element);
    $('.navigation-main li.active').removeClass('active');
    $('.nav-item li.active').removeClass('active');
    $(element).parent().addClass('active').siblings().removeClass('active');
}

function loadMenu() {
    $('.loader').css('display','block');
    
    var menu, rs = {}
    $.ajax({
        url: URL_API + '/menu',
        type: 'GET',
        dataType: 'json',
        success: function (rs) {
            $('.loader').css('display','none');
            if (rs.response.data.hasOwnProperty("menu")) {
                var hash = location.hash.substr(1);
                
                menu = rs.response.data.menu
                var x = 0;
                var classOpen = ""
                menu.forEach(dataMenu => {
                    var classActive = ""
                    if (dataMenu.submenu.length > 0) {
                        if(dataMenu.url == hash ){
                            classActive = " active "
                        }
                        html = '<li class="has-sub nav-item PM'+x+'"><a rel="" ><i class="' + dataMenu.icon + '"></i><span data-i18n="" class="menu-title">' + dataMenu.name + '</span></a><ul class="menu-content">';
                        dataMenu.submenu.forEach(datasub => {
                            
                            if(datasub.url == hash ){
                                classActive = "active"
                                classOpen = "PM"+x
                            }
                            html = html + '<li class="'+classActive+'"><a href="#' + datasub.url + '" onclick="goURL(\'' + datasub.url + '\', this);onActive(this)"  class="menu-item">' + datasub.name + '</a></li>'
                            classActive = "";
                        })
                        html = html + '</ul></li>'
                        menu_list.after(html)
                    } else {
                        menu_list.after('<li class="'+classActive+'"><a href="#' + dataMenu.url + '" onclick="goURL(\'' + dataMenu.url + '\', this);onActive(this)" ><i class="' + dataMenu.icon + '"></i><span data-i18n="" class="menu-title">' + dataMenu.name + '</span></a></li>');
                    }
                    classActive = "";
                    x++;
                });
                
                if(classOpen != ""){
                    $("."+classOpen).addClass(" open ");
                }
                
                
                
            }
        },
        error: function (request, error) {
            $('.loader').css('display','none');
            $("#msj_warning").show();
            $("#msj_warning").text("Request: " + JSON.stringify(request) + JSON.stringify(error))

        }
    });


}

function inArray(needle, haystack) {
    var length = haystack.length;
    for (var i = 0; i < length; i++) {
        if (typeof haystack[i] == 'object') {
            if (arrayCompare(haystack[i], needle)) return true;
        } else {
            if (haystack[i] == needle) return true;
        }
    }
    return false;
}
function goURL(URL, event) {
    
    
    var posible_country = URL.split("=")
    
    if (posible_country.length > 0){
        if(posible_country[0] == "country"){
            URL = ''
        }
    }
    var html;
    if (URL != '') {
        $.ajax({
            url: URL + '.html',
            type: 'GET',
            success: function (html) {
                $(FULL_LAYOUT).html(html);
            },
            error: function (request, error) {
                $.ajax({
                    url: "/modulos/dashboard/index.html",
                    type: 'GET',
                    success: function (html) {
                        $(FULL_LAYOUT).html(html);
                    },
                    error: function (request, error) {
                        console.log("Error (1)");
                    }
                });
    
            }
        });

    } else {
        $.ajax({
            url: "/modulos/dashboard/index.html",
            type: 'GET',
            success: function (html) {
                $(FULL_LAYOUT).html(html);
            },
            error: function (request, error) {
                console.log("Error (2)");
            }
        });
    }
}