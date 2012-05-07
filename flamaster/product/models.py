from datetime import datetime

from flask.ext.sqlalchemy.ext.hybrid import hybrid_property

from flamaster.app import db
from flamaster.core.utils import slugify
from flamaster.core.models import CRUDMixin


__all__ = ['Product', 'Price']


class Product(db.Model, CRUDMixin):
    __tablename__ = 'products'

    title = db.Column(db.String(512), nullable=False)
    _slug = db.Column(db.String(128), nullable=False, unique=True)
    teaser = db.Column(db.String(1024))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User',
                             backref=db.backref('products', lazy='dynamic'))

    def __init__(self, **kwargs):
        assert 'title' in kwargs
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)

    def __repr__(self):
        return "<Product: %r>" % self.title

    @hybrid_property
    def slug(self):
        return self._slug

    @slug.setter
    def slug(self, value):
        self._slug = slugify(self.created_at or self.updated_at, self.title)

    @classmethod
    def get_by_slug(cls, slug):
        return cls.query.filter_by(slug=slug).first_or_404()


class Price(db.Model, CRUDMixin):
    """ model storage for a price version for end product
    """
    __tablename__ = 'prices'
