from simple_ddl_parser import DDLParser


ddl = """

CREATE TABLE "material" (
  "id" SERIAL PRIMARY KEY,
  "title" varchar NOT NULL,
  "description" text,
  "link" varchar NOT NULL,
  "type" material_type,
  "additional_properties" json DEFAULT '{"key": "value"}',
  "created_at" timestamp DEFAULT (now()),
  "updated_at" timestamp
);

"""

result = DDLParser(ddl).run(group_by_type=True)
import pprint

pprint.pprint(result)
