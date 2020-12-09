$("#id_city").change(function () {
        const url = $("#cityForm").attr("data-areas-url");  // get the url of the `load_areas` view
        const cityId = $(this).val();  // get the selected city ID from the HTML input

        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= /ajax_load_areas/ )
            data: {
                'city_id': cityId       // add the city id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_areas` view function
                $("#id_area").html(data);  // replace the contents of the area input with the data that came from the server
            }
        });

    });
    $("#id_district").change(function () {
        const url = $("#districtForm").attr("data-cities-url");  // get the url of the `load_cities` view
        const districtId = $(this).val();  // get the selected district ID from the HTML input

        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= /ajax/load-cities/ )
            data: {
                'district_id': districtId       // add the district id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $("#id_city").html(data);  // replace the contents of the city input with the data that came from the server
                /*

                let html_data = '<option value="">---------</option>';
                data.forEach(function (city) {
                    html_data += `<option value="${city.id}">${city.name}</option>`
                });
                console.log(html_data);
                $("#id_city").html(html_data);

                */
            }
        });

    });