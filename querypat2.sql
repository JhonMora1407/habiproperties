CREATE TABLE user_property (
  id int(11) NOT NULL AUTO_INCREMENT,
  auth_user_id int(11) NOT NULL,
  property_id int(11) NOT NULL,
  like_property int(1) default 0,
  CONSTRAINT user_property_pk PRIMARY KEY (auth_user_id, property_id)
  CONSTRAINT user_fk FOREIGN KEY (auth_user_id) REFERENCES auth_user (id),
  CONSTRAINT property_id_fk FOREIGN KEY (property_id) REFERENCES property (id)
);

Se crea de esta forma para que exista la relacion cliente propieda y cada vez que se consulte por 