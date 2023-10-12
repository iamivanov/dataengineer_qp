CREATE TABLE ivanov_traps_raw (
	message json NULL,
	recieved timestamp NULL,
	"date" date NULL
)
WITH (
	appendonly=true,
	orientation=column
)
DISTRIBUTED RANDOMLY
PARTITION BY RANGE (date);

CREATE TABLE ivanov_traps_devices (
    id int8 NOT NULL,
    remote_device_id varchar(255) NULL,
    CONSTRAINT traps_devices_pkey PRIMARY KEY (id)
);

CREATE TABLE ivanov_traps_messages (
    id int8 NOT NULL,
    device_int8 NOT NULL,
    clock timestamp,
    CONSTRAINT traps_messages_pkey PRIMARY KEY (id),
    CONSTRAINT traps_devices_fkey FOREIGN KEY (device_id) REFERENCES ivanov_traps_devices(id)
);

CREATE TABLE ivanov_traps_oids (
 id int8 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE),
 "oid" varchar(255) NULL,
 value varchar(255) NULL,
 value_raw varchar(255) NULL,
 message_id int8 NULL,
 CONSTRAINT traps_oids_pkey PRIMARY KEY (id),
 CONSTRAINT traps_oids_fkey FOREIGN KEY (message_id) REFERENCES ivanov_traps_messages(id)
);
CREATE INDEX trap_definition_oid_idx ON ivanov_traps_oids USING btree (oid);













CREATE TABLE ivanov_traps_devices (
    id int8 NOT NULL,
    remote_device_id varchar(255) NULL,
    CONSTRAINT traps_devices_pkey PRIMARY KEY (id)
);

CREATE TABLE ivanov_traps_messages (
    id int8 NOT NULL,
    device_id int8 NOT NULL,
    clock timestamp,
    CONSTRAINT traps_messages_pkey PRIMARY KEY (id),
    CONSTRAINT traps_devices_fkey FOREIGN KEY (device_id) REFERENCES ivanov_traps_devices(id)
);

CREATE TABLE ivanov_traps_oids (
 id int8 NOT NULL,
 "oid" varchar(255) NULL,
 value varchar(255) NULL,
 value_raw varchar(255) NULL,
 message_id int8 NULL,
 CONSTRAINT traps_oids_pkey PRIMARY KEY (id),
 CONSTRAINT traps_oids_fkey FOREIGN KEY (message_id) REFERENCES ivanov_traps_messages(id)
);
CREATE INDEX trap_definition_oid_idx ON ivanov_traps_oids USING btree (oid);


CREATE TABLE ivanov_traps_devices (
    id int8 NOT NULL,
    remote_device_id varchar(255) NULL,
    CONSTRAINT traps_devices_pkey PRIMARY KEY (id)
);

CREATE TABLE ivanov_traps_messages (
    id int8 NOT NULL,
    device_id int8 NOT NULL,
    clock timestamp,
    CONSTRAINT traps_messages_pkey PRIMARY KEY (id),
    CONSTRAINT traps_devices_fkey FOREIGN KEY (device_id) REFERENCES ivanov_traps_devices(id)
);

drop table ivanov_traps_oids;

CREATE TABLE ivanov_traps_oids (
 id SERIAL PRIMARY KEY,
 "oid" varchar(255) NULL,
 value varchar(255) NULL,
 value_raw varchar(255) NULL,
 message_id int8 NULL,
 CONSTRAINT traps_oids_fkey FOREIGN KEY (message_id) REFERENCES ivanov_traps_messages(id)
);
CREATE INDEX trap_definition_oid_idx ON ivanov_traps_oids USING btree (oid);

delete from ivanov_traps_devices where 1=1;

select * from ivanov_traps_messages itm ;