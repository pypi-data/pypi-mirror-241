class Embed:
  def __init__(self, title = None, description = None, color = None, footer = None, image = None, thumbnail = None, author = None, author_icon = None, author_url = None, title_url = None, footer_icon = None, timestamp = None):
      self.title = title
      self.description = description
      self.color = color
      self.footer = footer
      self.image = image
      self.thumbnail = thumbnail
      self.author = author
      self.author_icon = author_icon
      self.author_url = author_url
      self.title_url = title_url
      self.footer_icon = footer_icon
      self.timestamp = timestamp

      self.content = {
              "title": self.title,
              "description": self.description,
              "color": self.color,
              "timestamp": self.timestamp,
              "url": self.title_url,
              "author": {
                  "name": self.author,
                  "url": self.author_url,
                  "icon_url": self.author_icon
              },
              "thumbnail": {
                  "url": self.thumbnail
              },
              "image": {
                  "url": self.image
              },
              "footer": {
                  "text": self.footer,
                  "icon_url": self.footer_icon
              },
              "fields": []
      }

  def add_field(self, name, value, inline = True):
    field_data = {
        "name": name,
        "value": value,
        "inline": inline
    }
    self.content.get('fields').append(field_data)

  def __call__(self):
    return self.content