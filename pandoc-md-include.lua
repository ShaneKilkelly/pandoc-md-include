-- Pandoc MD Include
-- '^<!%-%- %%%% include%("(.+)"%) %%%% %-%->$'

return {
  {
    RawBlock = function(elem)
      include_file = string.match(
        elem.text,
        '^<!%-%- %%%% include%("(.+)"%) %%%% %-%->$'
      )
      if include_file then
        -- dunno lol
      end
      return elem
    end,
  }
}
