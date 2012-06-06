# encoding: utf-8
require_relative 'string'

lat_str = "cereTlis quCa"
geo_str = "ცერეთლის ქუჩა"

puts "lat_str = 'cereTlis quCa'"
puts "geo_str = 'ცერეთლის ქუჩა'"
puts ""
puts "lat_str georgianized: #{lat_str.georgianize}"
puts "geo_str latinized: #{geo_str.latinize}"

puts lat_str.is_georgian? ? "lat_str is georgian characters" : "lat_str is not georgian characters"
puts lat_str.is_latin? ? "lat_str is latin characters" : "lat_str is not latin characters"
puts geo_str.is_georgian? ? "geo_str is georgian characters" : "geo_str is not georgian characters"
puts geo_str.is_latin? ? "geo_str is latin characters" : "geo_str is not latin characters"

#puts lat_str.georgian_morph('extended')
#puts geo_str.georgian_morph('extended')