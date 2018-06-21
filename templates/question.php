<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="/static/js/jquery-migrate-1.2.1.min.js" type="text/javascript"></script>
    <script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=LGzDQ41DTXiwNfGTyXVIEwGUTcPZMRAr"></script>
</head>
<body>
    <form id="question_form" action="" method="post" >

        <input type='hidden' name='lngvalue' id="lng_id" value="" />
        <input type='hidden' name='latvalue' id="lat_id" value="" />
        <input type="submit" name="subbtn" vaule="提交"/>
    </form>
</body>
</html>
<script type="text/javascript">
    var geolocation = new BMap.Geolocation();

	geolocation.getCurrentPosition(function(r){
		if(this.getStatus() == BMAP_STATUS_SUCCESS){
            document.getElementById("lng_id").value = r.point.lng;
            document.getElementById("lat_id").value = r.point.lat;
		}
		else {
			//alert('failed'+this.getStatus());
		}
	},{enableHighAccuracy: true})
</script>