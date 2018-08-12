-- slug no debe tener espacio
-- INSERT INTO catalogue_productclass(name,slug,requires_shipping,track_stock) VALUES('industriales','industriales',1,1);
-- INSERT INTO catalogue_productclass(name,slug,requires_shipping,track_stock) VALUES('semi-industriales','semi-industriales',1,1);
-- INSERT INTO catalogue_productclass(name,slug,requires_shipping,track_stock) VALUES('agricolas','agricolas',1,1);
-- INSERT INTO catalogue_productclass(name,slug,requires_shipping,track_stock) VALUES('tecnologia','tecnologia',1,1);

-- categorias
-- INSERT INTO catalogue_category(path,depth,numchild,name,description,image,slug) VALUES("001",1,0,'tecnologia',"<p>productos para uso profesional.</p>",,"categories/tecnologia.jpg","tecnologia");
-- INSERT INTO catalogue_category(path,depth,numchild,name,description,image,slug) VALUES("002",1,0,'industrial',"<p>productos para mantenimiento y limpieza de areas de produccion de fabricas.</p>","categories/industrial.jpg","industrial");
-- INSERT INTO catalogue_category(path,depth,numchild,name,description,image,slug) VALUES("003",1,0,'semi-industrial',"<p>productos de uso comercial e industrial.</p>","categories/semi-industrial.jpg","semi-industrial");
-- INSERT INTO catalogue_category(path,depth,numchild,name,description,image,slug) VALUES("004",1,0,'agricola',"<p>productos para agricultores.</p>","categories/agricola.jpg","agricola");


-- socios / partner 
-- INSERT INTO partner_partner(code,name) VALUES("diego-solis","Diego Solis");
-- INSERT INTO partner_partner(code,name) VALUES("diana-naranjo","Diana Naranjo");
-- INSERT INTO partner_partner(code,name) VALUES("juan-perez","Juan Perez");
-- INSERT INTO partner_partner(code,name) VALUES("maria-yagual","Maria Yagual");
-- INSERT INTO partner_partneraddress("title","first_name","last_name","line1","line2","line3","line4","state","postcode","search_text","country_id","partner_id") 
-- 	VALUES("","Diego","Solis","data de villamil","km 9 1/2 via a data de posorja","Data de Villamil","Playas","Guayas","EC090101","data de villamil km 9 1/2 via a posorja Data de Villamil Playas Guayas EC090101 Republic of Ecuador","EC",1);
-- INSERT INTO partner_partneraddress("title","first_name","last_name","line1","line2","line3","line4","state","postcode","search_text","country_id","partner_id") 
--	VALUES("","Diana","Naranjo","data de villamil","km 9 1/2 via a data de posorja","Data de Villamil","Playas","Guayas","EC090102","data de villamil km 9 1/2 via a posorja Data de Villamil Playas Guayas EC090102 Republic of Ecuador","EC",2);
-- INSERT INTO partner_partneraddress("title","first_name","last_name","line1","line2","line3","line4","state","postcode","search_text","country_id","partner_id") 
--	VALUES("","Juan","Perez","data de villamil","km 9 1/2 via a data de posorja","Data de Villamil","Playas","Guayas","EC090103","data de villamil km 9 1/2 via a posorja Data de Villamil Playas Guayas EC090103 Republic of Ecuador","EC",3);
-- INSERT INTO partner_partneraddress("title","first_name","last_name","line1","line2","line3","line4","state","postcode","search_text","country_id","partner_id") 
-- VALUES("","Maria","Yagual","data de villamil","km 9 1/2 via a data de posorja","Data de Villamil","Playas","Guayas","EC090104","data de villamil km 9 1/2 via a posorja Data de Villamil Playas Guayas EC090104 Republic of Ecuador","EC",4);


catalogue_product
catalogue_productcategory
catalogue_productimage
partner_stockrecord